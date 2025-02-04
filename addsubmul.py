numberfirst = input("Enter your number:  ")
numberfirst = int(numberfirst)
numbersecond = input("Enter your number:  ")
numbersecond = int(numbersecond)

operation = input("Choose operation (+, -, *, /):  ")

if operation == "+" :
    newnumber = numberfirst+numbersecond
    print(newnumber)
elif operation == "-":
    newnumber = numberfirst-numbersecond
    print(newnumber)
elif operation == "*":
    newnumber = numberfirst*numbersecond
    print(newnumber)
elif operation == "/" and numbersecond == 0:
    print("Error no division by 0")
elif operation == "/":
    newnumber = numberfirst/numbersecond
    print(newnumber)

#dowecontinue = input("Do you want to continue? (yes/no):")
while input("Do you want to continue? (yes/no):") == "yes" :
    numberthird = input("Enter your number:  ")
    numberthird = int(numberthird)
    operation2 = input("Choose operation (+, -, *, /):  ")
    if operation2 == "+" :
        newnumber = newnumber+numberthird
        print(newnumber)
    elif operation2 == "-":
        newnumber = newnumber-numberthird
        print(newnumber)
    elif operation2 == "*":
        newnumber = newnumber*numberthird
        print(newnumber)
    elif operation2 == "/" and numberthird == 0:
        print("Error no division by 0")
    elif operation2 == "/":
        newnumber = newnumber/numberthird
        print(newnumber)
print("the end")
