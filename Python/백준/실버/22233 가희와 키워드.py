import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.keyword = [input() for _ in range(self.n)]
        self.posts = [input() for _ in range(self.m)]

    def solve(self):
        keyword = set(self.keyword)

        for post in self.posts:
            for i in post.split(","):
                if i in keyword:
                    keyword.remove(i)

            print(len(keyword))


problem = Main()
problem.solve()
