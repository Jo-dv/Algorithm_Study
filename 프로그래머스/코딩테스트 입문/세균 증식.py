n, t = 2, 10


def solution(n, t):
    answer = [n]
    for i in range(t):
        answer.append(answer[-1] * 2)
    return answer[-1]


print(solution(n, t))
