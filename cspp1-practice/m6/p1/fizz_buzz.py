N = int(input())'''taking the input from user'''
I = 1
'''Iterating through the loop'''
while(I <= N):
    if(I % 3 == 0 and I % 5 == 0): '''checking if it is divisible by both 3 and 5'''
        print("Fizz")
        print("Buzz")
    elif(I % 3 == 0):'''checking if divisible by 3'''
        print("Fizz")
    elif(I % 5== 0):'''checking if divisible by 5'''
        print("Buzz")
    else:
        print(I)
    I = I + 1


    
