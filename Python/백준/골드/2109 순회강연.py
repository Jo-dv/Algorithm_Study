class Main:
    def __init__(self):
        self.n = int(input())
        self.schedule = [list(map(int, input().split())) for _ in range(self.n)]
        self.check = [0]
        self.answer = 0

    def solve(self):
        self.schedule.sort(key=lambda x: (x[1], -x[0]))
        cnt = 0
        for pay, day in self.schedule:
            rest_day = day - cnt
            if rest_day <= 0 or self.check[-1] == day:
                continue
            self.answer += pay
            self.check.append(day)
            cnt += 1

        print(self.answer)


problem = Main()
problem.solve()
