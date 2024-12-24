class Main:
    def __init__(self):
        self.str1 = input()
        self.str2 = input()
        self.answer = 0

    def solve(self):
        prev = [0] * (len(self.str2) + 1)  # 이전 행
        curr = [0] * (len(self.str2) + 1)  # 현재 행

        for i in range(1, len(self.str1) + 1):
            for j in range(1, len(self.str2) + 1):
                if self.str1[i - 1] == self.str2[j - 1]:
                    curr[j] = prev[j - 1] + 1
                    self.answer = max(self.answer, curr[j])
                else:
                    curr[j] = 0

            prev, curr = curr, prev  # 현재 행을 이전 행으로 교체

        print(self.answer)


problem = Main()
problem.solve()
