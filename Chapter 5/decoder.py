__author__ = 'JDucommun'
#Converts Unicode number values into a string of text

def main():
    print("This program converts a sequence of Unicode numbers into")
    print("a string of text.")

    #Get the message, punk.
    inString = input("Please enter the Unicode encoded message.")

    #Loop through each substring and build the Unicode message
    message = ""
    for numStr in inString.split():
        codeNum = eval(numStr)      #Converts digits to a number
        message = message + chr(codeNum)    #Concatenate char to msg

    print("\nThe decoded message is:", message)

main()