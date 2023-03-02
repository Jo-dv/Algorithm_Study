from functools import reduce

box, n = [10, 8, 6], 3

def solution(box, n):
    return reduce(lambda x, y: x * y, [i // n for i in box])

print(solution(box, n))