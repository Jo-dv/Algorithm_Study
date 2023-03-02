n = 6

def solution(n):
    D = [0] * (n+1)
    D[2] = 3
    D[4] = 11
    for i in range(6, n+1, 2):
        D[i] = (D[i-2] * D[i-4] + 8) % 1000000007
    return D[n]

print(solution(n))