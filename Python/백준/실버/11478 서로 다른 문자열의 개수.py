class Main:
    def __init__(self):
        self.s = input()

    def solve(self):
        sub = set()

        for i in range(len(self.s)):
            string = ""
            for j in range(i, len(self.s)):
                string += self.s[j]
                sub.add(string)

        print(len(sub))


problem = Main()
problem.solve()