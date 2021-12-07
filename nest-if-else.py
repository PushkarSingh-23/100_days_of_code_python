print('welcome to nested if else program!')
print("welcome to park foundation !")
age = int(input("enter your age :"))
if age > 15:
    print("You can proceed to height counter")
    height = int(input("Enter your height!"))
    if height >=120:
        print("you can proceed to go and visit")
    else:
        print("sorry cant go ahead")
else:
    print("sorry cant go ahead")