#!/usr/bin/python3
"""
This script runs a classic programming challenge called FizzBuzz.
"""

import sys  # Importing the sys module for reading command line arguments.

def fizzbuzz(n):
    """
    This function implements the FizzBuzz game.
    
    It takes one argument, n, and prints the numbers from 1 to n. However, there are some exceptions:
    - If the number is divisible by 3, it prints "Fizz".
    - If the number is divisible by 5, it prints "Buzz".
    - If the number is divisible by both 3 and 5, it prints "FizzBuzz".
    """

    if n < 1:  # If n is less than 1, the function returns without doing anything.
        return

    tmp_result = []  # This list will store the output.

    # Loop over the range from 1 to n inclusive.
    for i in range(1, n + 1):
        # If the number is divisible by both 3 and 5, append "FizzBuzz" to the list.
        if (i % 3) == 0 and (i % 5) == 0:
            tmp_result.append("FizzBuzz")
        # If the number is only divisible by 3, append "Fizz" to the list.
        elif (i % 3) == 0:
            tmp_result.append("Fizz")
        # If the number is only divisible by 5, append "Buzz" to the list.
        elif (i % 5) == 0:
            tmp_result.append("Buzz")
        # If the number is not divisible by 3 or 5, append the number itself (as a string) to the list.
        else:
            tmp_result.append(str(i))
    # Print all the elements in the list, joined by a space.
    print(" ".join(tmp_result))

# This makes sure that the script is being run directly, and not being imported as a module.
if __name__ == '__main__':
    # If no arguments were given, print an error message and usage instructions, then exit with a status code of 1.
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    # Convert the first command line argument to an integer, then pass it to the fizzbuzz function.
    number = int(sys.argv[1])
    fizzbuzz(number)
