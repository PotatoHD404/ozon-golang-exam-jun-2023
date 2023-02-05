import json
import time
import pathlib
import shutil


def main():
    base_path = pathlib.Path(__file__).parent
    with open('tasks.json', 'r') as f:
        tasks = json.load(f)
    for name, tests in tasks.items():
        # Create a directory for each task
        task_path = base_path / name
        task_path.mkdir(exist_ok=True)
        tests_path = task_path / 'tests'
        tests_path.mkdir(exist_ok=True)
        answers_path = task_path / 'answers'
        answers_path.mkdir(exist_ok=True)
        # Create a file for each test
        for i, test in enumerate(tests):
            test_path = tests_path / f'{i}.txt'
            with open(test_path, 'w') as f:
                f.write(test['input'])
            answer_path = answers_path / f'{i}.txt'
            with open(answer_path, 'w') as f:
                f.write(test['output'])
        # copy all files from templates to task directory
        for file in base_path.glob('templates/*'):
            file_path = task_path / file.name
            if not file_path.exists() and not file.as_posix().endswith('.old') and file.name != 'debug.cpp':
                shutil.copy(base_path / 'templates' / file, file_path)


if __name__ == '__main__':
    main()
