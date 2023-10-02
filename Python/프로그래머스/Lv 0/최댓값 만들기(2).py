numbers = [1, 2, -3, 4, -5]

def solution(numbers):
    numbers.sort()
    return max(numbers[0] * numbers[1], numbers[-2] * numbers[-1])

print(solution(numbers))