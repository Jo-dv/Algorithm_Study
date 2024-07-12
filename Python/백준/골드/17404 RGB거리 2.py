import copy
import math


class Main:
    def __init__(self):
        self.n = int(input())
        self.houses = [list(map(int, input().split())) for _ in range(self.n)]
        self.answer = math.inf
        
    def solve(self):
        for color in range(3):  # 각 색상에 대해
            cost = copy.deepcopy(self.houses)
            cost[0] = [math.inf] * 3  # 1번째 집 초기화
            cost[0][color] = self.houses[0][color]  # 색상별 집 고정 -> 선택된 값을 제외하고 큰 값을 가지므로 선택 불가

            for i in range(1, self.n):
                cost[i][0] += min(cost[i - 1][1], cost[i - 1][2])  # R
                cost[i][1] += min(cost[i - 1][0], cost[i - 1][2])  # G
                cost[i][2] += min(cost[i - 1][0], cost[i - 1][1])  # B
            cost[-1][color] = math.inf  # 첫 집과 마지막 집의 색상은 달라야하므로 처음에 선택된 집이 마지막에 선택되지 않도록 함
            self.answer = min(self.answer, min(cost[-1]))

        print(self.answer)


problem = Main()
problem.solve()