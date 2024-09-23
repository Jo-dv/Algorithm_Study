class Main:
    def __init__(self):
        self.n = int(input())
        self.distance = list(map(int, input().split()))
        self.costs = list(map(int, input().split()))
        self.answer = 0

    def solve(self):
        cost = self.costs[0]
        self.answer = cost * self.distance[0]  # 처음에는 무조건 주유소만큼 넣을 수 밖에 없음

        for i in range(1, self.n - 1):
            if cost > self.costs[i]:  # 항상 최저 코스트 보장
                cost = self.costs[i]

            self.answer += (cost * self.distance[i])

        print(self.answer)


problem = Main()
problem.solve()
