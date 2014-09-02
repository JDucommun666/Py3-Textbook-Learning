__author__ = 'JDucommun'


def main():
    print("Converting a textual message into a sequence of numbers")

    #getthemessagehere
    inString = input("Please enter your message to encode: ")

    #Build a unicode message
    chars = []
    for numStr in inString.split():
        codeNum = eval(numStr)  # Converts digits to a number
        chars.append(chr(codeNum))  # accumulate new character

        message = "".join(chars)
        print("\nThe decoded message is:", message)


main()
