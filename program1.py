import sys
import time

def process_task(args):
    # Simulating a time-consuming task
    time.sleep(2)

    # Perform some computation based on the arguments
    result = sum(args)

    return f"Result from program1.py: {result}"

if __name__ == '__main__':
    # Retrieve the arguments passed from the command line
    args = [int(arg) for arg in sys.argv[1:]]

    # Process the task
    result = process_task(args)

    # Print the result
    print(result)
