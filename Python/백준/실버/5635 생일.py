class Main:
    def __init__(self):
        self.n = int(input())
        self.students = [list(input().split()) for _ in range(self.n)]

    def solve(self):
        self.students.sort(key=lambda x: (-int(x[3]), -int(x[2]), -int(x[1])))

        print(self.students[0][0])
        print(self.students[-1][0])


problem = Main()
problem.solve()
