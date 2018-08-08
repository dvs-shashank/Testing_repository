# Exercise: Is In
# Write a Python function, isIn(char, aStr), that takes in two arguments a character and String and returns the isIn(char, aStr) which retuns a boolean value.

# This function takes in two arguments character and String and returns one boolean value.

def isIn(char, astr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
   
    le = len(astr)   
    #print("this is len",l)
    if le == 0:
        return False
    if le == 1:
        #print("le ==1  AND xhar is ",astr)
        if char == astr[0]:
            #print("char is :",char , "str is ",astr)
            return True
        else:
            return False
    else:
        mid = len(astr)//2
        #print(mid)
        if char == astr[mid]:
            return True
        elif char < astr[mid]:
            return isIn(char, astr[:mid])
        else:
            return isIn(char, astr[mid:])
        
   

def main():
    data = input()
    data = data.split()
    astr1 = sorted(data[1])
    print(isIn((data[0][0]), astr1))


if __name__== "__main__":
    main()
