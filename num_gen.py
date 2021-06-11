#!/usr/bin/env python3

# Created by: Jonathan Kene
# Created on: June 10, 2021
# The program places the numbers into a single variable
# and prints them to the console. After the array is full, your program
# calculates the average of all the numbers and displays it.

import random


def main():
    # this function uses an array
    list_of_int = []

    # input
    for loop_counter in range(0, 5):
        random_num = random.randint(10, 100)
        list_of_int.append(random_num)
    print("")

    for loop_counter in range(0, 5):
        average = sum(list_of_int)/len(list_of_int)
        print("{} added to the list at position"
              " {} ".format(list_of_int[loop_counter], loop_counter))
    print("")
    print("The average is {} ".format(average))


if __name__ == "__main__":
    main()
