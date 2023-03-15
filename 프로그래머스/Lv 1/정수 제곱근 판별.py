import math

n = 121

def solution(n):
    temp = math.sqrt(n)
    if temp % int(temp) == 0.0:
        answer = math.pow(math.sqrt(n) + 1, 2)
    else:
        answer = -1
    return answer

print(solution(n))