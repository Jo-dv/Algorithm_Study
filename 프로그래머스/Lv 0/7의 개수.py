array = [7, 77, 17]


def solution(array):
    return ''.join([str(i) for i in array]).count('7')


print(solution(array))
