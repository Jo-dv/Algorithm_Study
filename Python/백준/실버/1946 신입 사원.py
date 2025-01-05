import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.t = int(input())
        self.n = None
        self.test_case = None
        self.answer = None

    def solve(self):
        for _ in range(self.t):
            self.answer = 1  # 서류 1등
            self.n = int(input())
            self.test_case = [tuple(map(int, input().split())) for _ in range(self.n)]
            self.test_case.sort(key=lambda x: x[0])

            greater = self.test_case[0][1]
            for i in range(1, self.n):  # 면접 상위 점수자 찾기
                if greater > self.test_case[i][1]:  # 현재까지의 최상위보다 성적이 더 좋다면
                    self.answer += 1
                    greater = self.test_case[i][1]

            print(self.answer)


problem = Main()
problem.solve()