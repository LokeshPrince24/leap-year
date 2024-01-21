# Open the input file in read mode and output file in write mode
with open('input.txt', 'r') as infile, open('output5.txt', 'w') as outfile:
    # Read the years from the input file
    years = [int(year.strip()) for year in infile.readlines()]

    for Year in years:
        # Check if the year is a leap year
        if Year % 4 == 0: 
            outfile.write(str(Year) + ' is a leap year\n') 
        else: 
            outfile.write(str(Year) + ' is not a leap year\n') 
