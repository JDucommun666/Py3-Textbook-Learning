__author__ = 'JDucommun'
# calculate the actual roots of a quadratic equation
# illustrates use of math library
# Full exception clause builtin.

import math

def main():
    print("This program finds the real solutions to a quadratic")
    print()
    try:
        a, b, c = eval(input("Enter the coefficients (a, b, c): "))
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("The solutions are:", root1, root2 )
    except ValueError as exc0bj:
        if str(exc0bj) == "math domain error":
            print("No real roots.")
        else:
            print("\nYou didn't give me the right mixture of coefficients.")
    except NameError:
        print("\nYou don't know how to use the three seashells.")
    except TypeError:
        print("\nYour inputs weren't all numbers.")
    except SyntaxError:
        print("\nYo shit wasn't written right.  Where's your commas?")
    except:
        print("Fuck if I know...")

main()