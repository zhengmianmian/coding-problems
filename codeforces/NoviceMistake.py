"""
Round 957 (Div. 3)
E. Novice's Mistake
"""
def weird(n,a,b):
    s=str(n)
    n_len = len(s)
    final_len = n_len * a - b
    if final_len<1:
        return -1
    res = s * (final_len//n_len) + s[:final_len%n_len]
    return int(res) if len(res)>0 else -1

def solution(n):
    pairs = []
    for a in range(1,10001):
        s=''
        threshold = n*a
        s = str(n) * (len(str(threshold))//len(str(n))) + str(n)[:len(str(threshold))%len(str(n))]
        if len(s)>0 and int(s)>=threshold:
            s = s[:-1]
        if len(s)<1:
            continue
        b = n*a - int(s)
        while len(s)>0 and b>=1 and b<= min(10000, n*a):
            if weird(n,a,b)!=-1 and weird(n,a,b) == n*a-b:
                pairs.append((a,b))
            s=s[:-1]
            if len(s)>0:
                b = n*a - int(s)
    print(len(pairs))
    for p in pairs:
        print(p[0],' ',p[1])

if __name__=="__main__": 
    m=int(input())
    while m>0:
        n=int(input())
        solution(n)
        m-=1