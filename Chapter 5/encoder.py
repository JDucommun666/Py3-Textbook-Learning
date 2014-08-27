__author__ = 'JDucommun'

def main():
    print("Converting a textual message into a sequence of numbers")

    #getthemessagehere
    message = input("Please enter your message to encode: ")

    print("\nHere are the Unicode codes:")

    #Loop
    for ch in message:
        print(ord(ch), end=" ")

    print()

main()