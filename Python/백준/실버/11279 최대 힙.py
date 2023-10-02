from heapq import *
from sys import stdin

n = int(input())
arr = []
heapify(arr)  # 힙 생성

for _ in range(n):  # 단순 최대 힙 구현
    x = int(stdin.readline().rstrip())  # 일반 입력으로 받으면 시관초과 발생

    if x == 0:
        if not arr:
            print(0)
        else:
            print(heappop(arr)[1])  # 실제 값을 반환해야 하므로 [1]
    else:
        heappush(arr, (-x, x))  # 기본적으로 최소 힙이기 때문에 값에 음수를 붙여줌으로써 최대 힙 구현