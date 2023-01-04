#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: Dec 2022
# This program calculates your average mark


def average_mark(grades):
    # This function finds the average mark

    total = 0

    for grade in grades:
        total += grade

    average = round(total / len(grades), 2)

    return average


def main():
    # This function makes the list

    grades = []
    temp_int = None

    # Input
    print("This program calculates the average grade. Enter -1 to end.")
    print("")

    while True:
        try:
            temp_number = input("What is your mark (0 - 100): ")
            temp_int = int(temp_number)
            if temp_int < 100 and temp_int > 0:
                grades.append(temp_int)
            elif temp_int == -1:
                average = average_mark(grades)
                print("\nThe average is {0}%".format(average))
                break
        except ValueError:
            print("Invalid Input")
            continue

    print("\nDone.")


if __name__ == "__main__":
    main()
