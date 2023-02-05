import subprocess
import pathlib
import os


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def test_all():
    base_path = pathlib.Path(__file__).parent
    tests_path = base_path / 'tests'
    answers_path = base_path / 'answers'
    for i in range(len(os.listdir(tests_path))):
        test_path = tests_path / f'{i}.txt'
        answer_path = answers_path / f'{i}.txt'
        with open(test_path, 'r') as f:
            test = f.read()
        with open(answer_path, 'r') as f:
            answer = f.read()
        p = subprocess.Popen(['wsl', './main'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, cwd=base_path)
        out, err = p.communicate(test.encode())
        if out.decode() == answer:
            print(f'{Bcolors.OKGREEN}Test {i} passed{Bcolors.ENDC}')
        else:
            print(f'{Bcolors.FAIL}Test {i} failed{Bcolors.ENDC}')
            print(f'Expected: {answer}')
            print(f'Got: {out.decode()}')
