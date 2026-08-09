print("Welcome to roller Coaster")
height = int(input("what is your height in cm?"))
if height>=120:
    print("yay! You can ride")
    age = int(input("What is your age?"))
    if age<12:
        print("Please pay $5")
    elif age>=12 and age<=18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry! you can not ride")

#Can add any no. of elif conditions to check for the age and price.

