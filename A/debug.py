import subprocess
import pathlib
import os
import sys

from lib import test_all


def main():
    base_path = pathlib.Path(__file__).parent
    # Compile
    p = subprocess.Popen(['wsl', 'g++', '-std=c++17', '-o', './main', '-DLOCAL', './main.cpp'],
                         cwd=base_path, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    p.wait()

    p = subprocess.Popen(['wsl', './main'], stdin=sys.stdin, stdout=sys.stdout, cwd=base_path)
    p.wait()


if __name__ == '__main__':
    main()
