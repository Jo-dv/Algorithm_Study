array = [1, 8, 3]

def solution(array):
    return [max(array), array.index(max(array))]

print(solution(array))