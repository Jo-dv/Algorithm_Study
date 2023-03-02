a = [-1, 0, 1]
b = [1, 0, -1]


def solution(a, b):
    answer = 0

    for i, j in zip(a, b):
        answer += i * j
    return answer


print(solution(a, b))
