"""take input from user"""
N = int(input())
I = 1
"""checking while conditions"""
while(I <= N):
    """checking if conditions"""
    if(I % 3 == 0 and I % 5 == 0): 
        print("Fizz")
        print("Buzz")
    elif(I % 3 == 0):
        print("Fizz")
    elif(I % 5== 0):
        print("Buzz")
    else:
        print(I)
    I = I + 1



    
