s = '1 2 Z 3'

def solution(s):
    answer = []
    for i in s.split():
        answer.append(int(i)) if i != 'Z' else answer.pop()
    return sum(answer)

print(solution(s))