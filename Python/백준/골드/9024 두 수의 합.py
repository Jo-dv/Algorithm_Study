import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.t = int(input())
        self.n = self.k = 0
        self.s = None

    def solve(self):
        for _ in range(self.t):
            answer = 0
            self.n, self.k = map(int, input().split())
            self.s = list(map(int, input().split()))
            self.s.sort()
            low, high = 0, self.n - 1
            check = 10e9

            while low < high:
                temp = self.s[low] + self.s[high]
                if check > abs(temp - self.k):  # 범위가 더 좁혀지면 초기화
                    check = abs(temp - self.k)
                    answer = 1
                elif check == abs(temp - self.k):
                    answer += 1

                if temp < self.k:
                    low += 1
                elif temp > self.k:
                    high -= 1
                else:
                    low += 1
                    high -= 1

            print(answer)


problem = Main()
problem.solve()