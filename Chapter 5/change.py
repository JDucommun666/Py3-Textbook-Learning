__author__ = 'JDucommun'
# change.py
# A program to calc value of change in dollars mawfugga

def main():
    print("Change Counter")
    print()
    print("Enter the count of each coin type.")
    quarters = eval(input("Quarters: "))
    dimes = eval(input("Dimes: "))
    nickels = eval(input("Nickels: "))
    pennies = eval(input("Pennies: "))
    total = quarters * 25 + dimes * 10 + nickels * 5 + pennies
#    idiot1 = total//100
#    idiot2 = total%100
    print()
    print("The total value of your change is ${0}.{1:0>2}"
          .format(total//100, total%100))


#    print("The total value of your change is ${0:0.2f}".format(total))
#    print("The total value of  your dumb change is", total)
#    print("If you are a total idiot, that would mean that you have", idiot1, "whole dollars")
#    print("...and", idiot2, "cents left over.")

main()