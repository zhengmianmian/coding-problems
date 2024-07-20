
def moveable(s):
    return len(s)>0 and 'U' in s
def turn(c):
    return 'U' if c=='D' else 'D'
def move(s):
    n=len(s)
    pos = s.find('U')
    s = list(s)
    if n>2:
        # turn neighbors
        if pos==0:
            s[1] = turn(s[1])
            s[n-1] = turn(s[n-1])
        elif pos==n-1:
            s[0]=turn(s[0])
            s[n-2]=turn(s[n-2])
        else:
            s[pos-1]=turn(s[pos-1])
            s[pos+1]=turn(s[pos+1])
    s.pop(pos)
    return ''.join(s)

if __name__=="__main__": 
    n=int(input())
    while n>0:
        l=int(input())
        s=input()
        alice=True # whose turn
        while moveable(s):
            s=move(s)
            alice=not alice
        res= 'NO' if alice else 'YES'
        print(res)
        n-=1