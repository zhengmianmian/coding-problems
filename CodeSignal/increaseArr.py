def strictlyIncrease(sequence):
    cnt = 0
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i+1]:
            cnt = cnt +1
    if cnt>0:
        return False
    else:
        return True

def solution(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i+1]:
            # remove i
            subarray = sequence[0:i] + sequence[i+1:]
            subarray2 = sequence[0:i+1] + sequence[i+2:]
            if strictlyIncrease(subarray) or strictlyIncrease(subarray2):
                return True
            else:
                return False
    return True

my_list = [1, 2,63, 4, 5]

print(solution(my_list))

