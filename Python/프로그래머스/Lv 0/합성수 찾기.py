n = 10

def solution(n):
    answer = [[j for j in range(1, int(i**0.5)+1) if i % j == 0] for i in range(1, n+1)]
    return len(list(filter(lambda x: len(x) > 1, answer)))

print(solution(n))