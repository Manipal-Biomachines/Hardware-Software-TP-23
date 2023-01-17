"""
Problem-1
Create a Pseudo-Random Generator program that upon calling gives you a
unique number every time between 2 set limits and stores and arranges
all the generated numbers in a 2D array that's visible after each call.
"""
import sys
import random
import signal


def signal_handler(signal, frame):
    """ This is for the KeyboardInterrupt. """
    print("Exiting ...")
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)

    # Get input from user.
    LOWER_LIMIT = int(input("Enter lower limit: "))
    UPPER_LIMIT = int(input("Enter upper limit: "))

    SAMPLE_SPACE = range(LOWER_LIMIT, UPPER_LIMIT+1)

    array = []

    while True:
        proceed = input("Continue? (Y|N)")
        if proceed == "N":
            break

        random_number = random.randint(LOWER_LIMIT, UPPER_LIMIT)
        if random_number in array:
            continue

        array.append(random_number)
        print(random_number)

    print("I'm reachable.")
