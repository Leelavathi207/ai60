print("Welcome to roller Coaster")
height = int(input("what is your height in cm?"))
if height>=120:
    print("yay! You can ride")
else:
    print("Sorry! you can not ride")

#checking for the even number
a = int(input("Number you want to try"))
b = a%2
if b==0:
    print("even number")
else:
    print("Odd Number")


#Checking from the list
a = list(range(1,21))
i = 0
while i < len(a):
    i = i+1
    b = a[i-1]
    c = b%2
    if c==0:
        print("even number")
    else:
        print("Odd Number")
    

