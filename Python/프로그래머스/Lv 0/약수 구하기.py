n = 24

def solution(n):
    return [i for i in range(1, n+1) if n % i == 0]

print(solution(n))