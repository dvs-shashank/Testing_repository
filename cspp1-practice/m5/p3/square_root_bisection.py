"""Bisection method example program"""
NUM = int(input())
EPS = 0.01
LOW = 0
HIGH = NUM 
ANS = (HIGH + LOW)/2.0
while abs(ANS**2 - NUM) >=EPS:
    if ANS**2 < NUM:
        LOW = ANS
    else:
        HIGH = ANS
    ANS = (HIGH + LOW)/2.0
print(ANS)

