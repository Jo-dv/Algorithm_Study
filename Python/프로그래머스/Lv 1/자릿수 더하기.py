n = 123

def solution(n):
    temp = map(int, (str(n)))
    answer = sum(temp)

    return answer

print(solution(n))