__author__ = 'JDucommun'
# calculate the actual roots of a quadratic equation
# illustrates use of math library
# may crash if you're an idiot

import math

def main():
    print("This program finds the real solutions to a quadratic")
    print()

    a, b, c = eval(input("Enter the coefficients (a, b, c): "))
    
    discrim = b * b - 4 * a * c
    if discrim < 0:
        print("Equation has no real roots!")
    elif discrim == 0:
        root = -b / (2 * a)
        print("There is a double root at", root)
    else:
        discRoot = math.sqrt(discrim)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print()
        print("The mawfuggin' solutions are:", root1, root2 )

main()