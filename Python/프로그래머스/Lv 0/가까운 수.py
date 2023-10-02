array, n = [3, 10, 28], 20

def solution(array, n):
    answer = {i: abs(i - n) for i in array}
    return min(list(answer.items()), key=lambda x: (x[1], x[0]))[0]

print(solution(array, n))