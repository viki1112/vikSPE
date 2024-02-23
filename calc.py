#!/usr/bin/env python

import math
import argparse

def root(n):
    if n<0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    res=math.sqrt(n)
    print(res)
    return res

def factorial(n):
    if n<0:
        raise ValueError("Factorial is not defined for negative numbers.")
    res=math.factorial(n)
    print(res)
    return res

def log(n):
    if n<=0:
        raise ValueError("Logarithm is not defined for non-positive numbers.")
    res=math.log(n)
    print(res)
    return res

def power(base, exponent):
    res=math.pow(base,exponent)
    print(res)
    return res

# def main():
#     print("Enter an Operation: ")
#     print("1. Square Root")
#     print("2. Factorial")
#     print("3. Log")
#     print("4. Power")

#     choice = int(input("Enter Choice: "))

#     if choice==1:
#         root(float(input("Enter a number: ")))
#     elif choice==2:
#         factorial(int(input("Enter a number: ")))
#     elif choice==3:
#         log(float(input("Enter a number: ")))
#     elif choice==4:
#         power(float(input("Enter a number: ")), float(input("Enter the Exponent: ")))
#     else:
#         print("Invalid Operation")
def main():
    parser = argparse.ArgumentParser(description='Perform a mathematical operation.')
    parser.add_argument('operation', type=str, choices=['sqrt', 'fact', 'log', 'pow'],
                        help='The operation to perform: sqrt, fact, log, pow')
    parser.add_argument('number', type=float, help='The number (for sqrt, fact, log) or base (for pow)')
    parser.add_argument('--exponent', type=float, help='The exponent (required for pow operation)', default=1.0)

    args = parser.parse_args()

    if args.operation == 'sqrt':
        root(args.number)
    elif args.operation == 'fact':
        factorial(int(args.number))  # factorial expects an int
    elif args.operation == 'log':
        log(args.number)
    elif args.operation == 'pow':
        power(args.number, args.exponent)

if __name__=="__main__":
    main()
