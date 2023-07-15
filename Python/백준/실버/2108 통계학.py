'''
mode = Counter(arr).most_common()
mode = mode[1][0] if len(mode) >= 2 else mode[0][0]
# 길이가 2 이상일 때, 빈도를 비교하고 값을 선택해야 하는데 무조건적으로 두 번째로 작은 값을 선택해버림
'''

from collections import Counter
from sys import stdin

n = int(input())
arr = [int(stdin.readline().rstrip()) for _ in range(n)]
arr.sort()

mean = round(sum(arr) / n)
median = arr[(n-1) // 2]
mode = Counter(arr).most_common()
if n > 1:  # 길이가 2 이상일 때
    mode = mode[1][0] if mode[0][1] == mode[1][1] else mode[0][0]  # 첫 번째와 두 번째의 빈도를 비교해 같은면 두 번째 아니면 첫 번째
else:
    mode = mode[0][0]  # 길이가 하나라면 상관없이 무조건 첫 번째
ra = arr[-1] - arr[0]

print(mean)
print(median)
print(mode)
print(ra)