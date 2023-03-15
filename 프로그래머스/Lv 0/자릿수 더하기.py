n = 1234

def solution(n):
    return sum(list(map(int, list(str(n)))))

print(solution(n))