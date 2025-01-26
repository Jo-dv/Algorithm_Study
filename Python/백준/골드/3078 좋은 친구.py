import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n, self.k = map(int, input().split())
        self.names = [input() for _ in range(self.n)]
        self.answer = 0

    def solve(self):
        cnt = [0] * 21  # 이름 길이별 카운트

        for i in range(self.n):
            if self.k < i:  # 슬라이딩 윈도우
                cnt[len(self.names[i - self.k - 1])] -= 1

            self.answer += cnt[len(self.names[i])]
            cnt[len(self.names[i])] += 1  # 갱신

        print(cnt)
        print(self.answer)


problem = Main()
problem.solve()
