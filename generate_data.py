import os
import json
import glob

def collect_problems():
    """Collect problem metadata from .leetcode solution files."""
    problem_list = []
    # pattern matches both .py and .cpp files
    for path in glob.glob('.leetcode/*.*'):
        # Expect format: <id>.<title-with-dashes>.<ext>
        filename = os.path.basename(path)
        parts = filename.split('.')
        if len(parts) < 3:
            continue
        prob_id = parts[0]
        # title may contain dots if splitted incorrectly; join all but first and last
        title_parts = parts[1:-1]
        title = '.'.join(title_parts).replace('-', ' ')
        ext = parts[-1]
        problem = {
            "id": int(prob_id) if prob_id.isdigit() else prob_id,
            "title": title,
            "language": ext,
            "solution_path": os.path.join('.leetcode', filename)
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
