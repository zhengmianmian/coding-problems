def solution(inputString):
    reversed_string = inputString[::-1]
    print(reversed_string)
    if inputString == reversed_string:
        print('solution(inputString) = true')
    else:
        print('solution(inputString) = false')


solution('aabaa')