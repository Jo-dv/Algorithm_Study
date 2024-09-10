class Main:
    def __init__(self):
        self.lower = list(input())
        self.answer = "z" * 51

    def solve(self):
        for i in range(1, len(self.lower) - 1):
            for j in range(i + 1, len(self.lower)):
                left, mid, right = self.lower[:i], self.lower[i:j], self.lower[j:]
                left.reverse()
                mid.reverse()
                right.reverse()

                self.answer = min(self.answer, "".join(left + mid + right))

        print(self.answer)


problem = Main()
problem.solve()