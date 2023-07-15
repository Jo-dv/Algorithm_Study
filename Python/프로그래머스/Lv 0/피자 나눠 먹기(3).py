slice, n = 4, 12

def solution(slice, n):
    return n // slice + (1 if 0 < n % slice <= slice else 0)

print(solution(slice, n))
