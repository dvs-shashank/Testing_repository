print("enter your option")
varA=none
varB=none
option=int(input("1)only integer 2)string or integer 3)integer or string")
if(option==1):
               varA=int(input("enter  integer"))
               varB=input("enter integer")
               if(varA>varB):
                   print("bigger")
               elif(varA<varB):
                   print("smaller")
               elif(varA==varB):
                   print("equal")
if(option==2):
               varA=input("enter string ")
               varB=int(input("enter int "))
               if(type(varA)==type(str()) or type(varB)==type(str())):
                   print("Strings involved")

if(option==3):
               varA=int(input("enter int "))
               varB=input("enter string ")
               if(type(varA)==type(str()) or type(varB)==type(str())):
                   print("Strings involved")


   
