class Main:
    def __init__(self):
        self.n, self.k = map(int, input().split())
        self.cows = [int(input()) for _ in range(self.n)]

    def solve(self):
        last_seen = {}
        answer = -1

        for i in range(self.n):
            breed_id = self.cows[i]  # 현재 소의 id
            if breed_id in last_seen and i - last_seen[breed_id] <= self.k:  # 현재 id와 같은 소를 이전에 봤다면
                answer = max(answer, breed_id)  # 현재 소와 마지막으로 본 소의 거리를 확인하고 id가 큰 소로 갱신
            last_seen[breed_id] = i  # 현재 소의 위치

        print(answer)


problem = Main()
problem.solve()
