n = 12

def solution(n):
    temp = [False for _ in range(n + 1)]
    for i in range(1, n + 1):
        if n % i == 0:
            temp[i] = True
    answer = [i for i in range(len(temp)) if temp[i]]
    return sum(answer)

print(solution(n))