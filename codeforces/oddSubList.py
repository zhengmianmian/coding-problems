def solution(m):
    cnt=0
    i=0
    while i<len(m)-1:
        if m[i] > m[i+1]:
            cnt+=1
            i+=2
        else:
            i+=1
    return cnt

if __name__=="__main__": 
    n=int(input())
    while n>0:
        w=int(input())
        s=input()
        s=s.split(' ')
        m=[int(i) for i in s]
        print(solution(m))
        n-=1

