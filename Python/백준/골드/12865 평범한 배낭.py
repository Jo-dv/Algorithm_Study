class Main:
    def __init__(self):
        self.n, self.k = map(int, input().split())
        self.item = [list(map(int, input().split())) for _ in range(self.n)]
        self.bag = [0] * (self.k + 1)  # 무게별 가치를 저장할 리스트

    def solve(self):
        for w, v in self.item:  # 아이템 순서대로
            for i in range(self.k, w - 1, -1):  # 최대 무게에서 현재 아이템 무게까지
                self.bag[i] = max(self.bag[i], self.bag[i - w] + v)  # 현재 무게의 가치 비선택 or 선택

        print(self.bag[self.k])


problem = Main()
problem.solve()