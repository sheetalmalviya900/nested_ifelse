print("facebook")
print("create an account")
print("it's free and always will be")
name=input("first name:")
if(name>="a" and name<="z" or name>="A" and name<="Z"):
    print(name)
    surname=input("last name:")
    if(name>="a" and name<="z" or name>="A" and name<="Z"):
        print(surname)
        number=int(input("enter the mobile number"))
        if(number>=1000000000 and number<10000000000):
            print(number)
            password=int(input("enter the six digit number"))
            if(password>=100000 and password<1000000):
                print(password)
                b_date=int(input('enter the date only'))
                b_month=int(input("enter the birth month only"))
                b_year=int(input("enter the birrh year"))
                if (b_date>=1 and b_date<=31):
                   (b_month>=1 and b_month<=12)
                   (b_year>=1950 and b_year<=2021)
                   print(str(b_date)+"/"+str(b_month)+"/"+str(b_year))
                   gender=(input("enter the gender:"))
                   if(gender=="male" or gender=="female") or gender=="transgender":
                       print(gender)
                   else:
                        print("something is wrong")
                else:
                    print("b-date glt hai")
            else:
                print("invalid password")
        else:
            print("wrong number")
    else:
        print("wrong surname")
else:
    print("wrong name")
print("create an account ^_^")
