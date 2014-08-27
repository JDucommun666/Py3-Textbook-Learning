__author__ = 'JDucommun'
# An easier program to print the month abbreviation by number

def main():
    #months is a list used as a lookup table
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    n = eval(input("Enter the month number again (1-12): "))

    print("The abbreviated month is", months[n-1] + ".")

main()