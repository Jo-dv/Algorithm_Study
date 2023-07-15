from math import gcd

arr = [3,4,9,16]

def solution(arr):
    while len(arr) > 1:
        n, m = arr.pop(), arr.pop()
        arr.append((n * m)//gcd(n, m))

    return sum(arr)
# 모든 수의 최소공배수가 아니라 두 수의 최소공배수를 하나의 수로 하여 다른 수들과 두개씩 짝지어 최소공배수를 구하는 문제


print(solution(arr))