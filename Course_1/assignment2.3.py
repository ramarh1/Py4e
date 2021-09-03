#write a program to prompt the user for hours and rate per hour using input to compute
# gross pay.. use 35 hours and a rate of 2.75 hours to test the program.
# pay should be 96.26

# Asks user for hours

hrs = input("Enter hours: ")
rph = input("Enter rate per hour: ")

payrate = int(hrs) * float(rph)



print("Pay:", payrate)
# comma is used to print float, whereas + only prints strings
