__author__ = 'JDucommun'
# calculate the actual roots of a quadratic equation
# illustrates use of math library
# may crash if you're an idiot

import math

def main():
    print("This program finds the real solutions to a quadratic")
    print()
    try:
        a, b, c = eval(input("Enter the coefficients (a, b, c): "))
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("The mawfuggin' solutions are:", root1, root2 )
    except ValueError:
        print("\nNo Real Roots, Biaaaatch")

main()