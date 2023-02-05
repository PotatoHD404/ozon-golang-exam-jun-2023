import subprocess
import pathlib
import os
from lib import test_all


def main():
    base_path = pathlib.Path(__file__).parent
    # Compile
    p = subprocess.Popen(['wsl', 'g++', '-std=c++17', '-o', './main', '-DLOCAL', './main.cpp'],
                         cwd=base_path, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    p.wait()
    # Run
    tests_path = base_path / 'tests'
    answers_path = base_path / 'answers'
    i = int(input('Enter test number: '))
    test_path = tests_path / f'{i}.txt'
    answer_path = answers_path / f'{i}.txt'
    with open(test_path, 'r') as f:
        test = f.read()
    with open(answer_path, 'r') as f:
        answer = f.read()
    p = subprocess.Popen(['wsl', './main'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, cwd=base_path)
    out, err = p.communicate(test.encode())
    print(f'Got: \n{out.decode()}')
    print(f'Expected: \n{answer}')


if __name__ == '__main__':
    main()
