x, n = map(int, input().split())

def solution(x, n):
    answer = [x * i for i in range(1, n + 1)]
    return answer

print(solution(x, n))