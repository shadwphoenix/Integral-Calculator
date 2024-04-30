"""

Created on Mar 20, 2022
@author: kasra

I wanted to write a Python program to calculate the area under a given function
using the definition of an integral. I will implement the polynomial functions
easily and without the eval function but will implement others functions with eval function in python.

"""
# importing math operators for eval to have access to them
from math import *


def co_input():
    # making a list to store all user inputs
    nums = []

    print("Enter the coefficients")
    print("Enter N/n to stop")

    i = 0
    while True:

        # getting each coefficient and storing in a list with the same index and printing what co the user is entering
        num = input("a" + str(i) + ": ")
        i += 1
        # if user enters n as input it does not get added to the list and the loop stops
        if num == "n" or num == "N":
            break

        # each input is added to the list as a float
        nums.append(float(num))

    return nums


def pol_value(x, co):
    result = 0
    for i in range(len(co)):
        # evaluating each term and adding them together in result
        result += co[i] * (x ** i)

    return result


def integral_pol(s, e):
    # getting each coefficient from user and store in a list
    coefficients = co_input()
    # this is our tiny step in X direction can make smaller for more accuracy but makes the program slow
    dx = 0.0001
    area = 0

    while s <= e:
        # calculates the area under the function in each step and adds to the area
        area += pol_value(s, coefficients) * dx
        s += dx

    return area


def integral_other(s, e):
    # could also use this for polynomial functions
    fun = input("Enter your function: ")
    function = lambda x: eval(fun)
    # same tiny step from poly function
    dx = 0.0001
    area = 0

    while s <= e:
        # evaluate the value of function
        y = float(function(s))
        # area of rectangle the height is the function value and width is dx
        area += y * dx
        s += dx

    return area


def get_range():
    # gets start and end
    while True:
        s = float(input('Enter starting range for the integral function: '))
        e = float(input('Enter ending range for the integral function: '))
        # start must be smaller than e here to make sure the range is valid for integration
        if s <= e:
            return s, e
        else:
            # to show user they had an invalid range
            print('Invalid range')


if __name__ == "__main__":
    # storing menu selection from user
    no = -1
    # keeps running until the user exits the program
    while True:
        # printing equal signs makes the code more readable
        print("=============================")
        # printing list view of options for user
        print('Which type of function are you looking for')
        print('1) Polynomials')
        print('2) Other functions')
        print('0) Exit')
        no = input('enter the number for the function you want: ')
        print("=============================")

        # if statement for each input

        if no == '0':
            # jumps out of while true loop if user gives 0
            break
        elif no == '1':
            print('a0 + a1*x + a2*x**2 + a3*x**3 + ... + an*x**n')
            # made into a function to reduce duplicate code
            # r gets a tuple index 0 is start index 1 is end.
            r = get_range()
            print("The area under the function = " + str(round(integral_pol(r[0], r[1]), 5)))
        elif no == '2':
            r = get_range()
            print("The area under the function = " + str(round(integral_other(r[0], r[1]), 5)))
        else:
            # if user inputs any other number
            print('Invalid input')

