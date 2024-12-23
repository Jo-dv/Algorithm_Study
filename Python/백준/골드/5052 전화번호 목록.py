import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.t = int(input())
        self.n = None
        self.numbers = None

    def solve(self):
        for _ in range(self.t):
            self.n = int(input())
            self.numbers = [input() for _ in range(self.n)]
            self.numbers.sort()  # 길이가 짧은 순

            for i in range(self.n - 1):
                prefix = len(self.numbers[i])
                if self.numbers[i] == self.numbers[i + 1][:prefix]:  # 현재 값이 다음 값에 포함되어 있다면 전화 불가
                    print("NO")
                    break
            else:
                print("YES")


problem = Main()
problem.solve()
