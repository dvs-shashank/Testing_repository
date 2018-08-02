s=input()
s=s+" "
i=0
len1=-1
while i<(len(s)-2):
    temp=i
    while s[temp]<=s[temp+1] and (temp)<(len(s)-2):
        temp=temp+1
    len2=temp-i
    if len2>len1:
        len1=len2
        k=int(i)
        le=int(temp)
    i=temp+1
t1=k
t2=le
while k<=le:
    print(s[k])
    k=k+1
