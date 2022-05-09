#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: March 2022
# This program calculates the area of a triangle with functions


def percentage(user_level):
    # calculate temperature

    # process & output
    if user_level == "4+":
        number = 97
    elif user_level == "4":
        number = 89
    elif user_level == "4-":
        number = 80
    elif user_level == "3+":
        number = 78
    elif user_level == "3":
        number = 75
    elif user_level == "3-":
        number = 70
    elif user_level == "2+":
        number = 68
    elif user_level == "2":
        number = 64
    elif user_level == "2-":
        number = 60
    elif user_level == "1+":
        number = 58
    elif user_level == "1":
        number = 55
    elif user_level == "1-":
        number = 50
    elif user_level == "R":
        number == 30
    else:
        number == -1

    return number

def main():
    # This function gets input

    # input
    user_level = input("Enter your level and it shall be converted to a percentage: ")
    print("")

    # call functions
    percentages = percentage(user_level)

    # output
    print("Your percentage is {0} % ".format(percentages))
    print("\nDone.")

if __name__ == "__main__":
    main()
