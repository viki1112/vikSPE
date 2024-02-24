#!/usr/bin/python3

import math
# import argparse

def root(n):
#     if n<0:
#         raise ValueError("Cannot calculate the square root of a negative number.")
    res=math.sqrt(n)
    print(res)
    return res

def factorial(n):
    # if n<0:
        # raise ValueError("Factorial is not defined for negative numbers.")
    res=math.factorial(n)
    print(res)
    return res

def log(n):
    # if n<=0:
        # raise ValueError("Logarithm is not defined for non-positive numbers.")
    res=math.log(n,math.e)
    print(res)
    return res

def power(base, exponent):
    res=math.pow(base,exponent)
    print(res)
    return res

def main():
    print("Enter an Operation: ")
    print("1. Square Root")
    print("2. Factorial")
    print("3. Log")
    print("4. Power")

    choice = int(input("Enter Choice (1/2/3/4): "))

    if choice==1:
        num=float(input("Enter a number: "))
        root(num)
    elif choice==2:
        num=int(input("Enter a number: "))
        factorial(num)
    elif choice==3:
        num=float(input("Enter a number: "))
        log(num)
    elif choice==4:
        base=float(input("Enter a number: "))
        exponent=float(input("Enter the Exponent: "))
        power(base, exponent)
    else:
        print("Invalid Operation")

# def main():
#     parser = argparse.ArgumentParser(description='Enter an operation: ')
#     parser.add_argument('operation', type=str, choices=['1', '2', '3', '4'],
#                         help='The operation to perform: root, factorial, log, power')
#     parser.add_argument('number', type=float, help='The number (for root, factorial, log) or base (for pow)')
#     parser.add_argument('--exponent', type=float, help='The exponent (required for pow operation)', default=1.0)

#     args = parser.parse_args()

#     if args.operation == '1':
#         root(args.number)
#     elif args.operation == '2':
#         factorial(int(args.number))  # factorial expects an int
#     elif args.operation == '3':
#         log(args.number)
#     elif args.operation == '4':
#         power(args.number, args.exponent)

if __name__=="__main__":
    main()
