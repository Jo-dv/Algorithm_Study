n = 5

def solution(n):
    D = [0, 1, 2]
    for i in range(3, n+1):
        D.append((D[i-1] + D[i-2]) % 1000000007)
    return D[n]

print(solution(n))