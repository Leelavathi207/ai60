print("Welcome to roller Coaster")
height = int(input("what is your height in cm?"))
if height>=120:
    print("yay! You can ride")
    age = int(input("what is your age?"))
    if age<=18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry! you can not ride")
