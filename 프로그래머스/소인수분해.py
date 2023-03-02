n = 1100

def solution(n):
    answer = []

    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            answer.append(i)
            n /= i

    return answer

print(solution(n))