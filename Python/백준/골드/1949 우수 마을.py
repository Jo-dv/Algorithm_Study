import sys
sys.setrecursionlimit(10**5)
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n = int(input())
        self.resident = [0] + list(map(int, input().split()))
        self.nums = [tuple(map(int, input().split())) for _ in range(self.n - 1)]
        self.dp = [[0, 0] for _ in range(self.n + 1)]  # 우수마을이 아닌 경우, 우수마을인 경우의 주민수
        self.visited = [False] * (self.n + 1)

    def dfs(self, current, tree):
        self.visited[current] = True
        self.dp[current][1] = self.resident[current]

        for nxt in tree[current]:
            if not self.visited[nxt]:
                self.dfs(nxt, tree)
                self.dp[current][0] += max(self.dp[nxt][0], self.dp[nxt][1])  # 그냥 마을 일 때는 인접 마을이 우수인지 아닌지는 상관 없음
                self.dp[current][1] += self.dp[nxt][0]  # 우수 마을끼리는 인접하면 안 됨

    def solve(self):
        tree = {i: [] for i in range(self.n + 1)}
        for u, v in self.nums:
            tree[u].append(v)
            tree[v].append(u)

        self.dfs(1, tree)
        print(max(self.dp[1][0], self.dp[1][1]))


problem = Main()
problem.solve()