def solution(m):
    h,w = len(m), 0
    if h>0:
        w = len(m[0])
    res=[[0 for _ in range(len(m[0]))]for _ in range(len(m))]
    n = (min(w, h) + 1) // 2
    for i in range(n):
        TL = (i, i)
        TR = (i, w-1-i)
        BL = (h-1-i, i)
        BR = (h-1-i, w-1-i)
        # counter clockwise
        if i%2:
            if TL[1] != TR[1] and TL[0]!=BL[0]:
                res[TL[0]][TL[1]], res[TR[0]][TR[1]], res[BL[0]][BL[1]], res[BR[0]][BR[1]] = m[TL[0]][TL[1]+1], m[TR[0]+1][TR[1]], m[BL[0]-1][BL[1]], m[BR[0]][BR[1]-1] 
                # top & bottom
                for c in range(TL[1]+1, TR[1]):
                    res[i][c] = m[i][c+1] 
                    res[h-1-i][c] = m[h-1-i][c-1]
                # left & right
                for r in range(TL[0]+1, BL[0]):
                    res[r][i] = m[r-1][i]
                    res[r][w-1-i] = m[r+1][w-1-i]
            elif TL[1] == TR[1] and TL[0]!=BL[0]:
                # a single col
                res[BL[0]][BL[1]] = m[TL[0]][TL[1]]
                for r in range(TL[0], BL[0]):
                    res[r][TL[1]] = m[r+1][TL[1]]
            elif TL[1] != TR[1] and TL[0] ==BL[0]:
                # a single row
                res[TR[0]][TR[1]]= m[TL[0]][TL[1]]
                for c in range(TL[1], TR[1]):
                    res[TL[0]][c] = m[TL[0]][c+1] 
            else:
                res[TL[0]][TL[1]] = m[TL[0]][TL[1]]
        # clockwise
        else:
            if TL[1] != TR[1] and TL[0]!=BL[0]:
                res[TL[0]][TL[1]], res[TR[0]][TR[1]], res[BL[0]][BL[1]], res[BR[0]][BR[1]] = m[TL[0]+1][TL[1]], m[TR[0]][TR[1]-1], m[BL[0]][BL[1]+1], m[BR[0]-1][BR[1]] 
                # top & bottom
                for c in range(TL[1]+1, TR[1]):
                    res[i][c] = m[i][c-1] 
                    res[h-1-i][c] = m[h-1-i][c+1]
                # left & right
                for r in range(TL[0]+1, BL[0]):
                    res[r][i] = m[r+1][i]
                    res[r][w-1-i] = m[r-1][w-1-i]
            elif TL[1] == TR[1] and TL[0]!=BL[0]:
                # a single col
                res[TL[0]][TL[1]] = m[BL[0]][BL[1]]
                for r in range(TL[0]+1, BL[0]+1):
                    res[r][TL[1]] = m[r-1][TL[1]]
            elif TL[1] != TR[1] and TL[0] == BL[0]:
                # a single row
                res[TL[0]][TL[1]]= m[TR[0]][TR[1]]
                for c in range(TL[1]+1, TR[1]+1):
                    res[TL[0]][c] = m[TL[0]][c-1] 
            else:
                res[TL[0]][TL[1]] = m[TL[0]][TL[1]]
    return res

def print_matrix(m):
    for row in m:
        print(row)


m= [[238, 239, 240, 241, 242, 243, 244, 245]]

print_matrix(solution(m))