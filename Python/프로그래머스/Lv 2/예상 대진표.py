import math
N = 8
A = 4
B = 7

def solution(n,a,b):
    answer = 1
    while True:
        if answer == int(math.log2(n)) or a == b:
            return answer
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        if a == b:
            return answer
        answer += 1
        if abs(a - b) == 1 and math.ceil((a + b) / 2) % 2 == 0:
            return answer

print(solution(N, A, B))