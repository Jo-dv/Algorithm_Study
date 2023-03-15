numbers = [1, 2, 3, 4, 5]

def solution(numbers):
    answer = sorted(numbers)
    return answer[-1] * answer[-2]

print(solution(numbers))