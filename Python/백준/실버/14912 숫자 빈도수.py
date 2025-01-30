class Main:
    def __init__(self):
        self.n, self.d = map(int, input().split())
        self.answer = 0

    def solve(self):
        nums = ""
        for i in range(1, self.n + 1):
            nums += str(i)

        print(nums.count(str(self.d)))


problem = Main()
problem.solve()