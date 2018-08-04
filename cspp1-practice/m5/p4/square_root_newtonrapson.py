"""newton raphson method example program"""
EPS = 0.01
NUM = int(input())
GUESSING = NUM/2.0
while abs(GUESSING*GUESSING - NUM) >= EPS:
    GUESSING = GUESSING - (((GUESSING**2) - NUM)/(2*GUESSING))
print(GUESSING)