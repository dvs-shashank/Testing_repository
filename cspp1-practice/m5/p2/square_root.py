"""
square root approximation
"""
NUM = int(input())
EPS = 0.1
APRX = 0
APRX = int(APRX)
while NUM - (APRX*APRX) > EPS and APRX < NUM:
    if NUM - (APRX*APRX) > EPS:
        APRX = APRX+EPS
print(APRX)
