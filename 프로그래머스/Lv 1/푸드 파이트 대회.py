food = [1, 3, 4, 6]

def solution(food):
    answer = ''
    for i, j in enumerate(food):
        answer += str(i) * (j//2)

    return answer + '0' + ''.join(reversed(answer))

print(solution(food))