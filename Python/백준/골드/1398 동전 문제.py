class Main:
    def __init__(self):
        self.t = int(input())
        self.case = [int(input()) for _ in range(self.t)]

    def solve(self):
        dp = [0] * 101  # 데이터는 100의 배수로 증가 -> 즉 100원까지 1, 10, 25를 사용해 최소의 개수를 만들어 100의 배수 처리
        '''
        250111 = 250000 + 100 + 10 + 1
        = (25 * 100^2) + (100) + 10 + 1
        100단위로 나눠 작은 값으로 쪼개, 쪼갠 값을 독립적으로 처리하며 하나의 최적해를 구성하는 방식
        '''

        for i in range(1, 101):
            dp[i] = dp[i - 1] + 1
            if i - 10 >= 0:
                dp[i] = min(dp[i], dp[i - 10] + 1)
            if i - 25 >= 0:
                dp[i] = min(dp[i], dp[i - 25] + 1)

        for coin in self.case:
            answer = 0
            while coin > 0:
                answer += dp[coin % 100]
                coin //= 100

            print(answer)


problem = Main()
problem.solve()