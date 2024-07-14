import sys
input = lambda: sys.stdin.readline()


class Main:
    def __init__(self):
        self.n = int(input())
        self.nums = list(map(int, input().split()))
        self.m = int(input())
        self.query = [list(map(int, input().split())) for _ in range(self.m)]
        self.answer = [[0] * self.n for _ in range(self.n)]

    def init_table(self):
        for i in range(self.n):
            self.answer[i][i] = 1  # 한 자리는 무조건 팰린드롬
            
    def check_pair(self):
        for i in range(self.n - 1):  # 두 수를 비교했을 때 둘 다 동일하면 팰린드롬
            self.answer[i][i + 1] = 1 if self.nums[i] == self.nums[i + 1] else 0

    def check_rest(self):
        for i in range(self.n - 2):  # 3개 이상부터 n개까지 탐색
            for start in range(self.n - 2 - i):
                end = start + 2 + i
                if self.nums[start] == self.nums[end] and self.answer[start + 1][end - 1]:  # 끝이 같고 중간이 팰린드롬
                    self.answer[start][end] = 1

    def solve(self):
        self.init_table()
        self.check_pair()
        self.check_rest()

        for s, e in self.query:
            print(self.answer[s-1][e-1])


problem = Main()
problem.solve()