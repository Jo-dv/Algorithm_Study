class Main:
    def __init__(self):
        self.n = int(input())

    def solve(self):
        dp = [0] * 31
        dp[2] = 3

        for i in range(4, 31, 2):  # 홀수 길이는 만들 수 없음
            dp[i] = dp[i - 2] * dp[2]  # 기본식
            for j in range(i - 4, 1, -2):  # 다음 경우의 수를 계산할 때, 기본 조합 + 기본 조합이 아닌 기본 조합 + 유니크 조합으로
                dp[i] += dp[j] * 2  # 각 경우의 수를 합산, 기본조합: dp[j], 유니크 조합: 2, 기본조합끼리 하면 중복된 조합 발생
            dp[i] += 2  # 4 이상부터 새로운 형태의 유니크한 조합 2가지 고정적으로 발생
        # f(i) = f(i - 2) * f(2) + (f(i - 4) * 2 + f(i - 6) * 2 + ... f(i - k - 2) * 2 + f(i - k) * 2) + 2, 4 <= 2k < i
        # ex) f(8) = 6:2, 4:4, 2:6

        print(dp[self.n])


problem = Main()
problem.solve()
