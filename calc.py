#!/usr/bin/python3

import math

def root(n):
    res=math.sqrt(n)
    print(res)
    return res

def factorial(n):
    res=math.factorial(n)
    print(res)
    return res

def log(n):
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

if __name__=="__main__":
    main()
