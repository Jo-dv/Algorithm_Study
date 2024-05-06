n = 8

def solution(n):
    D = [0] * (n+1)
    D[2] = 3
    for i in range(4, n+1, 2):
        D[i] = (D[i-2] * 3 + (sum(D[:i-4+1]) * 2) + 2) % 1000000007
        # i-4+1: +1을 통해 합에 대한 인덱스 보정, 또한 각 n에 대해 새로 생기는 2개에 대한 경우의 수
    return D[n]

print(solution(n))