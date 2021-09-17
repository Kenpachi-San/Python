#!/usr/bin/python3

# Program name:calculator1.py
# Program purpose: Build a calculator
# Version: Python 3.9


print(" \n 1. Addition (+)\n 2. Subtraction (-)\n 3. Multiplication (*)\n 4. Division (/)\n")
operator = input("Select an operator (+, -, *, /): ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if operator == "+":
    print("--> Result of calculation: ", num1, "+", num2, "=", (num1 + num2))
elif operator == "-":
    print("--> Result of calculation: ", num1, "-", num2, "=", (num1 - num2))
elif operator == "*":
    print("--> Result of calculation: ", num1, "*", num2, "=", (num1 * num2))
elif operator == "/":
    if num2 == 0.0:
        print("Division by zero cannot be performed.")
    else:
        print("--> Result of calculation: ", num1, "/", num2, "=", (num1 / num2))

print("Thank you for using the program.")
