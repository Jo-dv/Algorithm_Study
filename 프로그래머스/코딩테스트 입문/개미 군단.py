hp = 23

def solution(hp):
    answer = 0
    for i in [5, 3, 1]:
        answer += divmod(hp, i)[0]
        hp = divmod(hp, i)[1]
    return answer

print(solution(hp))