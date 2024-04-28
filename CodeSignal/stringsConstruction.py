def countChar(a):
    m={}
    for c in a:
        if c in m:
            m[c] = m[c] +1
        else:
            m[c]=1
    return m

def solution(a, b):
    res=0
    ma = countChar(a)
    mb = countChar(b)
    for key in ma:
        if key not in mb:
            return 0
    for key in ma:
        ma[key] = mb[key] // ma[key]
    sorted_dict = dict(sorted(ma.items(), key=lambda item: item[1]))
    res = list(sorted_dict.values())[0]
    return res

a='abc'
b='aabbcc'
print(solution(a,b))


