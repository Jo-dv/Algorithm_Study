class Main:
    def __init__(self):
        self.n, self.k = map(int, input().split())
        self.medals = [list(map(int, input().split())) for _ in range(self.n)]

    def solve(self):
        self.medals.sort(key=lambda x: (-x[1], -x[2], -x[3]))
        rankings = {i: 1 for i in range(1, self.n + 1)}  # 기본 등수로 초기화, 처음엔 모두가 1등

        if self.n == 1:
            print(rankings[self.n])
        else:
            for i in range(1, self.n):  # 1등 다음부터 내 앞 등수랑 비교
                if self.medals[i - 1][1:] == self.medals[i][1:]:  # 앞 선수와 성적이 동일하면
                    rankings[self.medals[i][0]] = rankings[self.medals[i - 1][0]]  # 앞 선수 등수로 변경
                else:  # 성적이 차이가 난다면
                    rankings[self.medals[i][0]] = i + 1  # 앞에 있는 사람의 수 + 자기 자신

            print(rankings[self.k])


problem = Main()
problem.solve()