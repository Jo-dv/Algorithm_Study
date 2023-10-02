n = 10

def solution(n):
    temp = [True for _ in range(n + 1)]

    for i in range(2, int(n ** 0.5) + 1):
        if temp[i]:
            for j in range(i ** 2, n + 1, i):
                temp[j] = False

    answer = [i for i in temp[2:] if i]
    return len(answer)

print(solution(n))