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
    if discrim >= 0:
        discRoot = math.sqrt(discrim)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print()
        print("The mawfuggin' solutions are:", root1, root2 )
    else:
        print("\nThe equation has no real roots!  WTF asshole??!??")

main()