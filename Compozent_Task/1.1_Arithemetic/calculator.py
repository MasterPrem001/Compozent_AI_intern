usr_input= int(input("Choose the operation you want to perform  \n 1.Addition  \n 2.Subtraction  \n 3.Multiplication \n 4.Division :"))
if usr_input not in (1,2,3,4):
    print(" the Choice you've chosen is invalid try again")
    quit()
else:
    a = int(input("Enter the first Number:"))
    b = int(input("Enter the second Number:"))

    if (usr_input == 1) :
        sum= a + b
        print("the Result is :",sum)

    elif(usr_input ==2) :
        sum = a - b
        print("the Result is :",sum)

    elif(usr_input == 3) :
        sum = a * b
        print("the Result is :",sum)
    else:
        if (b == 0) :
            print("ZeroDivisionError: division by zero is not possible")
            quit()
        else:
            sum = a / b
            print("the Result is :",sum)
