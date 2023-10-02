sides = [11, 7]

def solution(sides):
    sides.sort()
    a = set(range(sides[1]-sides[0]+1, sides[1]+1))
    # 가장 긴 변 == max(sides): max(sides) < x + min(sides) -> max(sides) - min(sidex) < x <= max(sides)
    b = set(range(sides[1], sum(sides)))
    # 가장 긴 변 != max(sides): max(sides) <= x < sum(sides)
    # 패턴화: sum(sides) - max(sides) + min(sides) - 1
    return len(a | b)

print(solution(sides))