class Main:
    def __init__(self):
        self.s = int(input())

    def solve(self):
        n = target = 0

        while target <= self.s:
            n += 1  # 더해지는 수들의 수
            target += n  # 수들을 합산해서 만들어 낸 수

        print(n - 1)  # s를 넘기면 반복문이 종료되므로 그 이전 값이 최대 수


problem = Main()
problem.solve()