import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n, self.k, self.b = map(int, input().split())
        self.lights = [int(input()) for _ in range(self.b)]
        self.answer = float('inf')

    def solve(self):
        self.lights = set(self.lights)
        bit = [0] * self.n

        for i in range(self.n):
            if i + 1 not in self.lights:
                bit[i] = 1

        check = bit[:self.k].count(0)  # 모든 구간을 count로 계산하면 시간초과 발생
        for i in range(1, self.n - self. k + 1):
            if bit[i - 1] == 0:
                check -= 1
            if bit[i + self.k - 1] == 0:
                check += 1
            self.answer = min(self.answer, check)

        print(self.answer)


problem = Main()
problem.solve()