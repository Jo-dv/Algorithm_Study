n, k = 10, 3

def solution(n, k):
    d = k - n // 10
    return 12000 * n + 2000 * (0 if d < 1 else d)

print(solution(n, k))