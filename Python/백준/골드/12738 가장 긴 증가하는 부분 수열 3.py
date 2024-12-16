import bisect


class Main:
    def __init__(self):
        self.n = int(input())
        self.a = list(map(int, input().split()))

    def solve(self):
        lis = []
        for i in range(self.n):
            if not lis or lis[-1] < self.a[i]:
                lis.append(self.a[i])
            else:
                idx = bisect.bisect_left(lis, self.a[i])
                lis[idx] = self.a[i]

        print(len(lis))


problem = Main()
problem.solve()
