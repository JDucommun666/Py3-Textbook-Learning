__author__ = 'JDucommun'
# An easier program to print the month abbreviation by number

def main():
    #Date Conversion, bitche$
    #get that date
    dateStr = input("Enter a date (mm/dd/yyyy): ")

    #Split that b!tch
    monthStr, dayStr, yearStr = dateStr.split("/")

    #Get that month name
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
              "October", "November", "December"]
    monthStr = months[int(monthStr)-1]

    #Output the new format
    print("Using another method, the converted month is: ", monthStr, dayStr+",", yearStr)

main()
