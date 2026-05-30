import os
import json
import glob
import subprocess

def get_repo_url():
    """Return the HTTPS GitHub URL for this repository (owner/repo)."""
    try:
        # Get remote URL (supports both ssh and https forms)
        remote = subprocess.check_output(['git', 'config', '--get', 'remote.origin.url'], text=True).strip()
        # ssh: git@github.com:owner/repo.git
        # https: https://github.com/owner/repo.git
        if remote.startswith('git@'):
            # split after ':'
            _, path = remote.split(':', 1)
        elif remote.startswith('https://'):
            path = remote.split('https://github.com/', 1)[1]
        else:
            path = remote
        # Remove possible trailing .git
        if path.endswith('.git'):
            path = path[:-4]
        return f"https://github.com/{path}"
    except Exception:
        # Fallback to a placeholder; the site will still work for local testing
        return "https://github.com/unknown/unknown"

def collect_problems():
    """Collect problem metadata from .leetcode solution files."""
    problem_list = []
    base_url = get_repo_url()
    # pattern matches both .py and .cpp files
    for path in glob.glob('.leetcode/*.*'):
        # Expect format: <id>.<title-with-dashes>.<ext>
        filename = os.path.basename(path)
        parts = filename.split('.')
        if len(parts) < 3:
            continue
        prob_id = parts[0]
        title_parts = parts[1:-1]
        title = '.'.join(title_parts).replace('-', ' ')
        ext = parts[-1]
        solution_path = os.path.join('.leetcode', filename)
        # Build a URL that points to the file on GitHub (web view)
        solution_url = f"{base_url}/blob/main/{solution_path}"
        problem = {
            "id": int(prob_id) if prob_id.isdigit() else prob_id,
            "title": title,
            "language": ext,
            "solution_path": solution_path,
            "solution_url": solution_url,
        }
        problem_list.append(problem)
    # Sort by id numeric if possible
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
