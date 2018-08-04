"""program to find product of digits"""
N = int(input())
I = 1
COUNT = 0
PROD = 1
REM = 0
while N > 0:
    REM = N % 10
    if( REM > 0):
        PROD = PROD * REM
    N = N // 10    
    I = I + 1
print(PROD)
