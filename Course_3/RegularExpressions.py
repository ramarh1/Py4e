# Extracting data with regular expressions
import re

fname = input('Enter text file: ')
fh = open(fname)
total = 0

# goes through line in file
for line in fh:
    # only targets lines with numbers in them, filters through all other lines
    if re.search('\d+', line):
    
    # extracts lines with digits
        y = re.findall('\d+',line)

        for value in y:
            values = int(value)
            total += values
    


        

print(total)
    

