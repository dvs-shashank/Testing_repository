""" Program to print blank space for special chars"""
STR = input()
LE = len(STR)
I = 0
X = ""
while(I < LE):
    if (STR[I] == '!' or STR[I] == '@' or STR[I] == '#'):
        X = X + " "
    if (STR[I] == '$' or STR[I] == '%' or STR[I] == '^'):
        X = X + " "
    if (STR[I] == '&' or STR[I] == '*'):
        X = X + " "
    else:
        X = X + STR[I]
    I = I +1
print(X)

    
        
