class Main:
    def __init__(self):
        self.t = int(input())
        self.n = None
        self.sticker1 = None
        self.sticker2 = None

    def solve(self):
        for _ in range(self.t):
            self.n = int(input())
            self.sticker1 = list(map(int, input().split()))
            self.sticker2 = list(map(int, input().split()))
            sticker = [self.sticker1, self.sticker2]

            if self.n > 1:
                sticker[0][1] += sticker[1][0]
                sticker[1][1] += sticker[0][0]

            for i in range(2, self.n):
                sticker[0][i] += max(sticker[1][i - 1], sticker[1][i - 2])
                sticker[1][i] += max(sticker[0][i - 1], sticker[0][i - 2])

            print(max(sticker[0][-1], sticker[1][-1]))


problem = Main()
problem.solve()
