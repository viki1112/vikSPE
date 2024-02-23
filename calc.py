#!/usr/bin/env python

import math

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

def main():
    print("Enter an Operation: ")
    print("1. Square Root")
    print("2. Factorial")
    print("3. Log")
    print("4. Power")

    choice = int(input("Enter Choice: "))

    if choice==1:
        root(float(input("Enter a number: ")))
    elif choice==2:
        factorial(int(input("Enter a number: ")))
    elif choice==3:
        log(float(input("Enter a number: ")))
    elif choice==4:
        power(float(input("Enter a number: ")), float(input("Enter the Exponent: ")))
    else:
        print("Invalid Operation")

if __name__=="__main__":
    main()
