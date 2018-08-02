s=input()
count=0
le=len(s)
for i in range(0,le-2,1):
    temp=i
    if(s[temp]=='b' and s[temp+1]=='o' and s[temp+2]=='b'):
        count+=1
print(count)


