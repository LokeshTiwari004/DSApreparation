import os
import json
import glob
import subprocess

def get_repo_url():
    """Return the HTTPS GitHub URL for this repository (owner/repo)."""
    try:
        remote = subprocess.check_output(['git', 'config', '--get', 'remote.origin.url'], text=True).strip()
        # SSH URL: git@github.com:owner/repo.git
        # HTTPS URL: https://github.com/owner/repo.git
        if remote.startswith('git@'):
            # split after ':'
            _, path = remote.split(':', 1)
        elif remote.startswith('https://'):
            path = remote.split('https://github.com/', 1)[1]
        else:
            path = remote
        if path.endswith('.git'):
            path = path[:-4]
        return f"https://github.com/{path}"
    except Exception:
        return "https://github.com/unknown/unknown"

def load_difficulties():
    """Load difficulty levels from completed.txt. Returns dict mapping id->level (0/1/2)."""
    diff_map = {}
    if not os.path.exists('completed.txt'):
        return diff_map
    with open('completed.txt') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) >= 2:
                pid = parts[0]
                level = int(parts[1])
                diff_map[pid] = level
    return diff_map

def dashify(title):
    """Convert a title back to the dash‑case used for log filenames."""
    # lower case, replace spaces with hyphens, remove any extra punctuation
    return title.lower().replace(' ', '-').replace('_', '-')

def collect_problems():
    """Collect problem metadata from .leetcode solution files and build URLs."""
    problem_list = []
    base_repo = get_repo_url()
    raw_base = base_repo.replace('https://github.com/', 'https://raw.githubusercontent.com/') + '/main/'
    diff_map = load_difficulties()
    for path in glob.glob('.leetcode/*.*'):
        filename = os.path.basename(path)
        parts = filename.split('.')
        if len(parts) < 3:
            continue
        prob_id = parts[0]
        title_parts = parts[1:-1]
        title = '.'.join(title_parts).replace('-', ' ')
        ext = parts[-1]
        solution_path = os.path.join('.leetcode', filename)
        solution_url = f"{base_repo}/blob/main/{solution_path}"
        solution_raw_url = f"{raw_base}{solution_path}"
        # Build expected log filename
        log_filename = f"{prob_id}.{dashify(title)}.md"
        log_path = os.path.join('logs', log_filename)
        log_raw_url = None
        if os.path.exists(log_path):
            log_raw_url = f"{raw_base}{log_path}"
        difficulty = diff_map.get(prob_id, 0)
        problem = {
            "id": int(prob_id) if prob_id.isdigit() else prob_id,
            "title": title,
            "language": ext,
            "difficulty": difficulty,
            "solution_path": solution_path,
            "solution_url": solution_url,
            "solution_raw_url": solution_raw_url,
            "log_raw_url": log_raw_url,
        }
        problem_list.append(problem)
    problem_list.sort(key=lambda x: (x['id'] if isinstance(x['id'], int) else float('inf')))
    return problem_list

def main():
    data = collect_problems()
    os.makedirs('data', exist_ok=True)
    with open('data/problems.json', 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Collected {len(data)} problems into data/problems.json")

if __name__ == '__main__':
    main()

