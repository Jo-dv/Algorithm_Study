class Main:
    def __init__(self):
        self.answer = []
        
    def solve(self):
        for _ in range(3):
            target = 0
            coins = []

            for _ in range(int(input())):
                coin, amount = map(int, input().split())
                target += coin * amount
                coins.append([coin, amount])

            if target % 2 == 1:
                self.answer.append(0)
                continue

            target //= 2
            dp = [False] * (target + 1)
            dp[0] = True

            result = 0
            for c in coins:
                coin, amount = c

                for t in range(target, coin-1, -1):
                    if dp[t - coin]:  # 특정 시점의 target인 t가 됐을 때, t를 coin으로 만들 수 있으면
                        for i in range(1, amount + 1):  # 해당 coin에서 target까지 coin의 수를 곱해가며 체크
                            if t - coin + (coin * i) <= target:  # t에는 이미 coin에 대한 값이 포함되어 있으므로 제거
                                dp[t - coin + (coin * i)] = True
                            else:
                                break

                if dp[-1]:  # 목표를 달성했다면
                    result = 1
                    break

            self.answer.append(result)

        for i in self.answer:
            print(i)


problem = Main()
problem.solve()

