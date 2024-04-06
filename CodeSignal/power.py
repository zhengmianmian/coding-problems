import math

def solution(n):
    if n==1:
        return True
    else:
        for a in range(2,round(math.sqrt(n))+1):
            b=2
            while math.pow(a,b)<n:
                b=b+1
            if math.pow(a,b)==n:
                return True
        return False

