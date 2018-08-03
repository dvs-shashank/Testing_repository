guessing=1
n=int(input())
flag=0
while (guessing<n+1):
    if(guessing**3==n):
        print(str(n) + " " + "is a perfect cube")
        flag=1
        break
    guessing=guessing+1
if(flag==0):
    print(str(n) + " " + "is not a perfect cube")
