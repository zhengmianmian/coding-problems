def solution(n):
    i=1
    t=1
    while t<n:
        i = i+1
        t = t * i
    return t

print(solution(17))