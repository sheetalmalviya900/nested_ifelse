upper_case=(input("enter the upper later :"))
if(upper_case>="A" and upper_case<="Z"):
    print("it's upper case")
    lower_case=(input("enter the lower later"))
    if(lower_case>="a" and lower_case<="z"):
        print("it's lower case")
        ch=(input("enter the special character"))
        if(ch=="@"  or ch=="#" or ch=="$" or ch=="%" or  ch=="&"):
            print("it's special character")
            num=int(input("enter the number"))
            if(num>=0 and num<=9):
                print("it's the number")
                if(len("6")):
                    print("done process")
                else:
                    print("invalid length")
            else:
                print("invalid number")
        else:
            print("invalid character")
    else:
        print(" invalid lower case")
else:
    print("invalid upper case")
password=(upper_case+lower_case+ch+str(num))
print(password)