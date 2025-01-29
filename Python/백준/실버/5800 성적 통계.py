class Main:
    def __init__(self):
        self.k = int(input())
        self.info = [list(map(int, input().split()))[1:] for _ in range(self.k)]

    def solve(self):
        for i in self.info:
            i.sort(reverse=True)

        for i, data in enumerate(self.info, 1):
            gap = -1
            for j in range(len(data) - 1):
                gap = max(gap, data[j] - data[j + 1])
            print(f'Class {i}')
            print(f'Max {data[0]}, Min {data[-1]}, Largest gap {gap}')


problem = Main()
problem.solve()
