__author__ = 'JDucommun'

def main():

    #This string is used as a lookup table
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"

    n = eval(input("Enter a month number (1-12): "))

    #Find the starting position
    pos = (n-1) * 3

    #Snatch that slice!
    monthAbbrev = months[pos:pos+3]

    #   Return Result
    print("The month you've specified is: ", monthAbbrev)

main()