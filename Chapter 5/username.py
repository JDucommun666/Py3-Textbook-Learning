__author__ = 'JDucommun'

def main():
    print("This program makes usernames.\n")

    #Get their name
    first = input("Please enter your first name lowercase")
    last = input("Please enter your last name lowercase")

    #concatenate it
    uname = first[0] + last[:7]

    print("Your username is: ", uname)

main()
