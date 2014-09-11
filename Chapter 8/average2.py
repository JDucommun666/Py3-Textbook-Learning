__author__ = 'JDucommun'

def main():
    sum = 0.0
    count = 0
    moredata = "yes"
    while moredata[0] == "y":
        x = eval(input("Enter a number >> "))
        sum = sum + x
        count = count + 1
        moredata = input("Do you have more (y/n)? ")
    print("\nThe average of the numbers so far is", sum / count)

main()