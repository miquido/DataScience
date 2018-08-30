import os
import sys


def run_container():
    print(sys.version)
    print('Im in: ', os.getcwd())
    print(os.listdir(os.getcwd()))


if __name__ == '__main__':
    run_container()

