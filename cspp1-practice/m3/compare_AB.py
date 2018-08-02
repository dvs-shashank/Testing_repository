option=int(input("1)int 2)string and int 3)int and string"))
if(option==1):
    varA=int(input("enter number"))
    varB=int(input("enter number"))
    if(varA>varB):
        print("bigger")
    elif(varA<varB):
        print("small")
    else:
        print("equal")
if(option==2):
    varA=input("enter string")
    varB=int(input("number"))
    if(type(varA)==type(str()) or type(varB)==type(str())):
        print("string involved")
if(option==3):
    varA=int(input("number"))
    varB=input("string")
    if(type(varA)==type(str()) or type(varB)==type(str())):
        print("string involved")
