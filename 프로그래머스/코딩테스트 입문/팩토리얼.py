from math import factorial

n = 7

def solution(n):
    return [i for i in range(1, 11) if factorial(i) <= n][-1]
    # n의 범위는 정수 1 ~ 10으로 고정, 그렇기에 fac(i)를 1씩 올려가며 n과 비교(i는 n이하), 마지막 값이 가장 근접한 팩토리얼 값

print(solution(n))