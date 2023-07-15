n = 18

def solution(n):
    answer = []
    for i in range(1, n + 1):
        if i**2 == n:
            answer.append(i)
            continue
        if n % i == 0:
            answer.append(i)

    return answer

print(solution(n))