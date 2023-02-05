import subprocess
import pathlib
import os
from lib import test_all


def main():
    base_path = pathlib.Path(__file__).parent
    # Compile
    p = subprocess.Popen(['wsl', 'g++', '-std=c++17', '-o', './main', './main.cpp'],
                         cwd=base_path, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    p.wait()
    # Run
    test_all()


if __name__ == '__main__':
    main()
