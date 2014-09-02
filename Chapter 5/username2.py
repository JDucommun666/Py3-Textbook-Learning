__author__ = 'JDucommun'

def main():
    print("This program makes usernames from a file of names.\n")

    # Get their name
    infileName = input("What file are their names in? ")
    outfileName = input("What file should their usernames go in?")

    # Open the files
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    # Process each line of the input file
    for line in infile:
        # get the first and last names from each line
        first, last = line.split()
        # Create the username
        uname = (first[0] + last[:7]).lower()
        # write that b!tch
        print(uname, file=outfile)

    # Close the files
    infile.close()
    outfile.close()


    print("Usernames built successfully to: ", outfileName)

main()
