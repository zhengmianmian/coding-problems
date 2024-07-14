_IN_RANGE = lambda x, y, h, w: 0 <= x < h and 0 <= y < w

NEIGHBOR_SHIFTS = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1,0],
    [1,1]
]

def solution(matrix):
    
    h, w = len(matrix), len(matrix[0])
    res = [[0 for j in range(w)] for i in range(h)]
    for i in range(h):
        for j in range(w):
            cnt=0
            for s in NEIGHBOR_SHIFTS:
                ii=i+s[0]
                jj=j+s[1]
                if _IN_RANGE(ii,jj,h,w) and matrix[ii][jj]:
                    cnt+=1
            res[i][j]=cnt

    return res




matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]

print(solution(matrix=matrix))