import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n = int(input())
        self.students = [input().split() for _ in range(self.n)]

    def solve(self):
        self.students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

        for i in self.students:
            print(i[0])


problem = Main()
problem.solve()
