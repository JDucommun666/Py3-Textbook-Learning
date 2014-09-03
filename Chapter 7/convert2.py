__author__ = 'JDucosmmun'

def main():
    print("Welcome to convert.py!")
    print("I take your Celsius and turn it into Fahrenheit.")
    celsius = eval(input("Enter the temperature in Celsius! "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

    #Warnings
    if fahrenheit > 90:
        print("It's really hot out there.  Grab some water!")
    if fahrenheit < 30:
        print("Wow.  Nipple Alert!")

main()