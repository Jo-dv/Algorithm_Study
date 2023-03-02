from collections import deque

numbers, direction = [1, 2, 3], "right"

def solution(numbers, direction):
    dir = {'left': -1, 'right': 1}
    answer = deque(numbers)
    answer.rotate(dir[direction])
    return list(answer)

print(solution(numbers, direction))