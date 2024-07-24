"""
Round 957 Div. 3
F. Valuable Cards
    find all divisors
    maintain a set of divisors of product in current segment(self and product)
    no 2 divisor apppears in one segment
   !!!
    I had assumed that the products of 2 divisors of x such that the product < x will still be a divisor of x. 
    This is clearly wrong (consider x to be 24, the divisors to be 2 and 8, 16<24 but 16 is not a divisor of 24). 
    Thus, my curr set contains unnecessary numbers increasing its size outside of the permissible bound.
"""
import math
def get_all_divisors(x):
    d=set()
    for i in range(1, int(math.sqrt(x))+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return d
def solution(x, m):
    divisors = get_all_divisors(x)
    pos = set() # boundary positions
    segment_divisors = set()
    stop=set() # stop when meeting an element in this set
    visit = [False for _ in range(len(m))]
    if m[0] in divisors:
        stop.add(x//m[0])
        segment_divisors.add(m[0])
    for i in range(1,len(m)):
        # print(m[i], ' stop: ',stop, ' segment divisors: ', segment_divisors)
        if m[i] in stop and not visit[i]:
            stop.clear()
            stop.add(x//m[i])
            segment_divisors.clear()
            segment_divisors.add(m[i])
            pos.add(i)
            visit[i] = True
        if m[i] in divisors and not visit[i]:
            stop.add(x//m[i])
            temp_set=set()
            for d in segment_divisors:
                if d*m[i] in divisors:
                    stop.add(x//(d*m[i]))
                    temp_set.add(d*m[i])
            segment_divisors.add(m[i])
            segment_divisors.update(temp_set)
            visit[i] = True
    # print('------------------------------')
    # print('boundary',pos)
    # print('------------------------------')
    print(len(pos)+1)

if __name__ == '__main__':
    t=int(input())
    while t>0:
        s=input()
        p=[int(i) for i in s.split(' ')]
        n,x=p[0],p[1]
        s2=input()
        m=[int(i) for i in s2.split(' ')]
        solution(x,m)
        t-=1
    # solution(36, [6,6,6,6])
    # solution(12,[12,1])
    

