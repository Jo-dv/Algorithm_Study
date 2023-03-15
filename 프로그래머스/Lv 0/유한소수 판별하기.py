import math

a, b = 11, 22

def solution(a, b):
    b //= math.gcd(a, b)
    for i in [2, 5]:
        while b % i == 0:  # 2로 최대한 나누고, 5로 최대한 나눠서
            b //= i
    return 1 if b == 1 else 2  # 1이 됐다면 유한소수 아니라면 무한소수


print(solution(a, b))
