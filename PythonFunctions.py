# Python Version 3.7

from tkinter import messagebox
from ctypes import *

# File path to C file
so_file = '/Users/ali/Desktop/CalculateHyp.so'

my_function = CDLL(so_file)
my_function.calculateHyp.restype = c_double


# Used for speedChecker function
class LessThanZeroException(Exception):
    pass


# Used for speedChecker function
class FloatInputException(Exception):
    pass


# Filters a list and returns elements that are of type float.
def fOnly(a_list):
    return [x for x in a_list if isinstance(x, float)]


# Returns a list of composite numbers up to num
def fNonPrimes(num):
    return [i for i in range(3, num + 1) if any([x for x in range(2, i) if i % x == 0])]


# Determines the amount of a fine for speeding
def speedChecker():
    try:
        speed_limit_value = input("Enter the speed limit:")
        speed_value = input("Enter your speed:")
        if isfloat(speed_limit_value) or isfloat(speed_value):
            raise FloatInputException
        speed_limit = int(speed_limit_value)
        speed = int(speed_value)
        if speed_limit < 0 or speed < 0:
            raise LessThanZeroException
        fine = 0
        if speed >= speed_limit:
            fine += 500
        if speed >= speed_limit + 6:
            fine += 600 * min(speed - (speed_limit + 5), 15)
        if speed >= speed_limit + 21:
            fine += 2000 * (speed - (speed_limit + 20))
        if speed > 400:
            fine = 0
        print("Your fine is: $" + str(fine))
    except LessThanZeroException:
        print("Numbers cannot be less than zero")
    except FloatInputException:
        print("Numbers cannot be float")
    except ValueError:
        print("String is not a number")


# Helper function for speedChecker
def isfloat(value):
    try:
        return float(value) and '.' in value
    except ValueError:
        return False


# Used tkinter to display a hello world message box
def helloWord():
    messagebox.showinfo("Window", "Hello world")


# Calls a C function to calculate the hypotenuse of a right-angled triangle
def funFunction():
    num1 = input("Enter float:")
    num2 = input("Enter float:")
    num1 = bytes(num1, "utf-8")
    num2 = bytes(num2, "utf-8")
    answer = my_function.calculateHyp(num1, num2)
    if answer == -1.0:
        return "Invalid values"
    else:
        return answer


