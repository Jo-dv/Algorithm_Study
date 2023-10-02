left = 13
right = 17

def solution(left, right):
    temp = [1 if len([j for j in range(1, i + 1) if i % j == 0]) % 2 == 0 else -1 for i in range(left, right + 1)]
    answer = [i * j for i, j in zip(temp, range(left, right + 1))]
    return sum(answer)

print(solution(left, right))