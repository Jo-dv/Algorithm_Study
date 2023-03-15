n = 15


def solution(n):
    answer = 0
    for i in range(1, n + 1):  # n까지 순서대로 순회
        temp = 0
        for j in range(i, n + 1):  # i부터 n까지 순서대로 순회
            if temp < n:  # temp가 n보다 작으면
                temp += j
            else:  # n을 넘었을경우
                break
        if temp == n:  # temp가 n이면
            answer += 1

    return answer


print(solution(n))
