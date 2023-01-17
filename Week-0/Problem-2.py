"""
Problem-2
Download a Random text file from "Lorem Ipsum".
Write a program to parse through the text and arrange all the words in
dictionary order and give the word count next to each word.
For example: Lorem: 7
Where Lorem is the word and 7 is the number of times it appears in the text file.
Export the final result as a .txt file and label it as "Problem_2_result.txt"
"""
import sys
import signal
from collections import Counter


def signal_handler(signal, frame):
    """ Handler function for the KeyboardInterrupt. """
    print("\nExiting now ...")
    sys.exit(0)


def using_counter(words_list):
    """
    Uses the Counter library to count ossurences in an array.
    """
    # Counts the occurences of an iterable.
    counter = Counter(words_list)

    # Returns in a list-like format that's already sorted in descending order.
    return counter


def using_dicts(words_list):
    """
    Just count the occurences and store in a dictionary.
    """
    counter = {}  # Initialise an empty dictionary.

    for word in words_list:
        # Check whether the counter contains an entry of the word.
        if word not in counter:
            counter[word] = 0

        # Increment the count of the word.
        counter[word] += 1

    # The dictionary at this point is not sorted according to the occurences.
    return counter


if __name__ == '__main__':
    # For the KeyboardInterrupt
    signal.signal(signal.SIGINT, signal_handler)

    with open('LOREM_IPSUM.txt', encoding='utf-8') as FILE:
        # By default, usually files are encoded in 'utf-8' format.
        # It's an optional parameter, but good practice to include.

        # Read the contents of the file
        contents = FILE.read()

        # Remove whitespaces on either sides of file.
        contents = contents.strip()

        # Convert the string to a list of words by
        # splitting the paragraph with " " spaces.
        contents = contents.split(" ")

        # Remove full stops from the end of words.
        # string.rstrip(param) removes the `param` from the rigth most side.
        contents = [word.rstrip(".") for word in contents]

        # Consider all words in lowercase only.
        contents = [word.lower() for word in contents]

    # Approach using regular dictionaries
    counts_dict = using_dicts(contents)
    print("Using regular dictionaries:\n", counts_dict)
    print()  # New line in between.

    # Approach using the Counter library
    counts_dict = using_counter(contents)
    print("Using Counter library:\n", counts_dict)
