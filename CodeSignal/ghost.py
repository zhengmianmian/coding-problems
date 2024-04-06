def solution(matrix):
    x = len(matrix)
    y = len(matrix[0])
    cnt=0
    for j in range(y):
        for i in range(x):
            if matrix[i][j]==0:
                break
            else:
                cnt = cnt + matrix[i][j]
    return cnt


matrix = [[0,1,1,2], 
 [0,5,0,0], 
 [2,0,3,3]]
print(solution(matrix))