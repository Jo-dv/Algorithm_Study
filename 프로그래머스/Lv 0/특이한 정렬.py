numlist, n = [1, 2, 3, 4, 5, 6], 4

def solution(numlist, n):
    return sorted(numlist, key=lambda x: (abs(x-n), -x))

print(solution(numlist, n))