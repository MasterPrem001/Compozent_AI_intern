def Palindrome(a):
    #empty input checker
    if a == '':
        print("User input is empty")
    else:
        #making sure that function will work even if has some capital letter's 
        a = a.lower()
        #reversing the string     
        b = a[::-1]
        #comparing original input and reversed string (if palindrome it will be same)    
        if a == b:
            print("The string you've entered is an Palindrome :",a)
        else:
             print("The string you've entered is not an Palindrome :",a)

    #Taking the user's input and using the function
Palindrome(input("Enter the String to Check if it is Palindrome:"))