sides = [1, 2, 3]

def solution(sides):
    sides.sort()
    return 1 if sides[-1] < sum(sides[:-1]) else 2

print(solution(sides))