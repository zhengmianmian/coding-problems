def can_jump_log(river,i,m):
    if i+m-1>=len(river):
        return i+m-1
    for ii in range(i,i+m):
        if river[2*i+m-ii-1]=='L':
            return 2*i+m-ii-1
    return -1
def can_jump_water(river,i,m):
    for ii in range(i,i+m):
        if i+m-1>=len(river):
            return i+m
        else:
            if river[2*i+m-1-ii]=='W':
                return 2*i+m-ii-1
    return -1
"""
n,
m:jump,
k:swim,
river: string LWC...
"""
def solution(p, river):
    n,m,k=p[0],p[1],p[2]
    res=True
    step=-1
    swam=0
    state='L'
    while step <n:
        i=step+1
        if state=='L' and can_jump_log(river,i,m)!=-1:
            step=can_jump_log(river,i,m)
            state='L'
        elif state=='L' and can_jump_water(river,i,m)!=-1:
            step=can_jump_water(river,i,m)
            state='W'
        elif state=='W' and swam<k and i<n and (river[i]=='L' or river[i]=='W'):
            swam+=1
            state=river[i]
            step=i
        elif state=='W' and swam<k and i==n:
            swam+=1
            state='L'
            step=i
        else:
            break
        
    res=True if step >=n else False
    return 'YES' if res else 'NO'

if __name__=="__main__": 
    n=int(input())
    while n>0:
        s=input()
        s=s.split(' ')
        a=[int(i) for i in s]
        river=input()
        res = solution(a, river)
        print(res)
        n-=1
    # a=[6, 6, 1]
    # river='WCCCCW'
    # print(solution(a,river))