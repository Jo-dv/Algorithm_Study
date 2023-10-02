def solution(a, b):
    answer = 0
    if a == b:
        return a
    elif a > b:
        lower = b
        upper = a
    else:
        lower = a
        upper = b
    for i in range(lower, upper + 1):
        answer += i
    return answer