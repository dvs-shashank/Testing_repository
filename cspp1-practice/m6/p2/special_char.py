'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''

   
STR = input()
LE = len(STR)
I = 0
X = ""
while(I < LE):
    if (STR[I]=='!' or STR[I]=='@' or STR[I]=='#' or STR[I]=='$' or STR[I]=='%' or STR[I]=='^' or STR[I]=='&' or STR[I]=='*'):
        X = X + " "
    else:
        X = X + STR[I]
    I = I +1
print(X)

    
        
 
