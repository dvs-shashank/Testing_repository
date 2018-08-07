# Exercise: GCDIter
# Write a Python function, gcdIter(a, b), that takes in two numbers and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.


def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    
    gcd=0
    for i in range(a):
    	if a%i==0:
    		factor_a[]=i
    for i in range (b):
    	if(b%i==0):
    		factor_b[]=i
    if a<b:
    	min[]=factor_a[]
    else:
    	min[]=factor_b[]
    for i in range (min[]):
    	if min[i]%a==0:
    		gcd=x

 


def main():
    data = input()
    data = data.split()
    print(gcdIter(int(data[0]),int(data[1]))) 

if __name__== "__main__":
    main()