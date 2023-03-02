from itertools import combinations

numbers = [-2, 3, 0, 2, -5]

def solution(number):
    return len([i for i in list(combinations(number, 3)) if sum(i) == 0])

print(solution(numbers))