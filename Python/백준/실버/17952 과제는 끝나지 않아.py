import sys
input = lambda: sys.stdin.readline()

class Main:
    def __init__(self):
        self.n = int(input())
        self.info = [list(map(int, input().split())) for _ in range(self.n)]
        self.stack = []
        self.answer = 0

    def solve(self):
        for i in self.info:
            if len(i) > 1:  # 수행할 과제가 있다면
                self.stack.append(i)  # 추가

            if self.stack:  # 과제들이 있다면
                self.stack[-1][2] -= 1  # 최근 과제 수행
                if self.stack[-1][2] == 0:  # 과제 다하면
                    self.answer += self.stack.pop()[1]  # 점수 획득

        print(self.answer)


problem = Main()
problem.solve()