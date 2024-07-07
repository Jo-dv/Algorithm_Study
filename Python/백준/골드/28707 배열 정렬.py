import math
from heapq import *


class Node:
    def __init__(self, value, cost):
        self.value = value
        self.cost = cost

    def __lt__(self, other):  # 클래스를 heapq에 넣어 정렬하려면 기준을 세워야 함
        return self.cost < other.cost


class Main:
    def __init__(self):
        self.n = int(input())
        self.arr = list(map(int, input().split()))
        self.m = int(input())
        self.operations = [list(map(int, input().split())) for _ in range(self.m)]

    def dijkstra(self, arr):
        hq = [Node(arr, 0)]
        cost = {tuple(arr): 0}  # 딕셔너리 키를 튜플로 변경 -> 키는 불변 객체여야 함

        while hq:
            current = heappop(hq)

            for l, r, c in self.operations:
                value = current.value[:]
                value[l - 1], value[r - 1] = value[r - 1], value[l - 1]
                value_tuple = tuple(value)  # 연산 후, 키 등록을 위해 불변 객체로 변환

                if current.cost + c < cost.get(value_tuple, math.inf):  # 키가 없으면 오류가 발생하므로 디폴트를 지정
                    cost[value_tuple] = current.cost + c
                    heappush(hq, Node(value, current.cost + c))

        print(cost.get(tuple(sorted(arr)), -1))

    def solve(self):
        self.dijkstra(self.arr)


problem = Main()
problem.solve()