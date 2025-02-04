from collections import defaultdict


class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())

    def solve(self):
        group = defaultdict(list)
        info = defaultdict(list)

        for _ in range(self.n):
            name = input()
            num = int(input())
            for _ in range(num):
                celeb = input()
                group[name].append(celeb)
                info[celeb].append(name)

            group[name].sort()

        for _ in range(self.m):
            name = input()
            num = int(input())

            if num == 0:
                for i in group[name]:
                    print(i)
            else:
                print(*info[name])


problem = Main()
problem.solve()