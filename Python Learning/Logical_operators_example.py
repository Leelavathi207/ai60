print("Welcome to roller Coaster")
height = int(input("what is your height in cm?"))
bill = 0
if height>=120:
    print("yay! You can ride")
    age = int(input("What is your age?"))
    if age<12:
        bill = 5
        print("Child tickets are $5")
    elif age>=12 and age<=18:
        bill = 7
        print("Youth tickets are $7")
    elif age >= 45 and age <= 55:
        #this condition can also be written as elif 45 <= age <= 55:
        bill = 0
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12")
    want_photo = input("Do you want a photo taken? type 'Y' for yes and 'N' for No.")
    if want_photo == "y":
        #Add $3 to their bill
        bill = bill + 3
        # can also write bill += 3
        #skipping the else statement as we don't need to do anything if they don't want a photo.
    print(f"Your final bill is ${bill}")
else:
    print("Sorry! you can not ride")


