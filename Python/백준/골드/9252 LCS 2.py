class Main:
    def __init__(self):
        self.string1 = " " + input()
        self.string2 = " " + input()

    def solve(self):
        n = len(self.string1)  # 열
        m = len(self.string2)  # 행
        lcs = [[""] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                if self.string2[i] == self.string1[j]:
                    lcs[i][j] = lcs[i - 1][j - 1] + self.string1[j]
                else:
                    lcs[i][j] = lcs[i][j - 1] if len(lcs[i][j - 1]) > len(lcs[i - 1][j]) else lcs[i - 1][j]

        answer = len(lcs[-1][-1])
        print(answer)
        if answer != 0:
            print(lcs[-1][-1])


problem = Main()
problem.solve()
