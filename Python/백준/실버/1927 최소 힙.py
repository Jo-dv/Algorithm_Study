from heapq import *
from sys import stdin

n = int(input())
arr = []
heapify(arr)

for _ in range(n):  # 단순히 heapq 라이브러리를 사용할 수 있는지 확인하는 문제, 직접 구현할 필요 x
    x = int(stdin.readline().rstrip())

    if x == 0:
        if not arr:
            print(0)
        else:
            print(heappop(arr))
    else:
        heappush(arr, x)