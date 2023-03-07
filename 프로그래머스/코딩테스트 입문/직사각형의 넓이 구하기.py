dots = [[1, 1], [2, 1], [2, 2], [1, 2]]

def solution(dots):
    dots = sorted(dots)
    return abs(dots[2][0] - dots[0][0]) * abs(dots[1][1] - dots[0][1])

print(solution(dots))