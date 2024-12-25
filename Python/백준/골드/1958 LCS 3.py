class Main:
    def __init__(self):
        self.str1 = input()
        self.str2 = input()
        self.str3 = input()
        self.answer = 0

    def solve(self):
        lcs = [[[0] * (len(self.str3) + 1) for _ in range(len(self.str2) + 1)] for _ in range(len(self.str1) + 1)]

        for i in range(1, len(self.str1) + 1):
            for j in range(1, len(self.str2) + 1):
                for k in range(1, len(self.str3) + 1):
                    if self.str1[i - 1] == self.str2[j - 1] == self.str3[k - 1]:
                        lcs[i][j][k] = lcs[i - 1][j - 1][k - 1] + 1
                    else:
                        lcs[i][j][k] = max(lcs[i - 1][j][k], lcs[i][j - 1][k], lcs[i][j][k - 1])

                    self.answer = max(self.answer, lcs[i][j][k])

        print(self.answer)


problem = Main()
problem.solve()

