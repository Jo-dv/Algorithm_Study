class Main:
    def __init__(self):
        self.items = list(map(int, input().split()))
        self.answer = 0

    def solve(self):
        a, b, c, d, e = self.items
        self.answer = e + d
        a -= d  # a랑 d는 한 묶음이므로 d를 담은만큼 제거

        while c > 0:
            self.answer += 1
            if b > 0:  # 3 + 2
                b -= 1
                c -= 1
            elif a > 0:  # 3 + 1 + 1
                a -= 2
                c -= 1
            else:  # 3
                c -= 1

        while b > 0:
            self.answer += 1
            if b > 1 and a > 0:  # 4 + 1
                b -= 2
                a -= 1
            elif b > 0 and a > 0:  # 2 + 1 + 1 + 1
                b -= 1
                a -= 3
            else:  # 2
                b -= 2

        while a > 0:  # 담을 a가 남아있다면
            self.answer += 1
            a -= 5

        print(self.answer)


problem = Main()
problem.solve()