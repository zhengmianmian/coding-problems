def solution(inputArray):
    res = float('-inf')
    for i in range(len(inputArray) - 1):
        if inputArray[i] * inputArray[i+1] > res:
            res = inputArray[i] * inputArray[i+1]
    print(res)

solution([3, 6, -2, -5, 7, 3])