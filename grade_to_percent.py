#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: March 2022
# This program takes a level and shows the percentage


def percentage(level):
    # calculate temperature

    # process & output
    if level == "4+":
        number = 97
    elif level == "4":
        number = 89
    elif level == "4-":
        number = 80
    elif level == "3+":
        number = 78
    elif level == "3":
        number = 75
    elif level == "3-":
        number = 70
    elif level == "2+":
        number = 68
    elif level == "2":
        number = 64
    elif level == "2-":
        number = 60
    elif level == "1+":
        number = 58
    elif level == "1":
        number = 55
    elif level == "1-":
        number = 50
    elif level == "R":
        number = 30
    else:
        number = -1

    return number


def main():
    # This function gets input

    # input
    level = input("Enter the grade and it shall be converted to a percentage: ")
    print("")

    # call functions
    percentages = percentage(level)

    # output
    print("{1} will have a percentage of {0} ".format(percentages, level))
    print("\nDone.")


if __name__ == "__main__":
    main()
