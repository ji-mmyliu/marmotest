import subprocess, sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

PROBLEM_NAME = 'current'
BIN = sys.argv[1]

case = 1

print("---Starting Marmotest Testcase Generation---")
while True:
    try:
        with open(f'testdata/{PROBLEM_NAME}/{case}.in', 'r') as fi, open(f'testdata/{PROBLEM_NAME}/{case}.out', 'w') as fo:
            exp = fo.read()
            testing_process = subprocess.run(BIN, stdin=fi, capture_output=True)
            print(f"Test case #{case}:", end=' ')
            if testing_process.returncode != 0:
                print(f"{bcolors.FAIL}ERROR{bcolors.ENDC}: Fatal error occurred during testing:", testing_process.stderr)
                exit(-1)
            stdout = testing_process.stdout.decode()
            if stdout == exp:
                print(f"{bcolors.OKGREEN}CORRECT{bcolors.ENDC}")
            else:
                print(f"{bcolors.WARNING}INCORRECT{bcolors.ENDC}")
                print(f"Your output:\n{stdout}")
                print(f"Expected output:\n{exp}")
                exit(1)
    except FileNotFoundError:
        break
    case += 1

print(f"---Marmotest Generation for problem {PROBLEM_NAME} succeeded---")