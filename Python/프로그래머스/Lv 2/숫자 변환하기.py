def solution(x, y, n):  # 백준의 정수를 1로 만들기와 유사
    dp = [1000001 if i != x else 0 for i in range(y+1)]  # x를 제외하고 임의의 최댓값으로 설정

    for i in range(x, y+1):  # x부터 시작해서 각 연산에 대한 값이 y를 넘기지 않는 하에
        if i + n <= y:
            dp[i + n] = min(dp[i + n], dp[i] + 1)
        if i * 2 <= y:
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)
        if i * 3 <= y:
            dp[i * 3] = min(dp[i * 3], dp[i] + 1)
        # dp[i] + 1은 i에 대한 연산 횟수 + 해당 시점에서의 추가 연산 +1이라는 의미
        # 연산 후와 연산 전 +1을 비교하는 이유: 초기 무한에 가까운 값에서 연산 횟수와 덮어쓰겠다는 의미인 동시에
        # i가 돌다가 x+n 시점에 도달했을 때 이미 연산 횟수가 있는 경우 최소 연산을 유지하기 위함
        # 예를 들어 i가 15에서 +5를 하여 20에 접근했을 때, 이미 i가 10일 때 x2를 통해 접근하여 연산 횟수를 덮어썼으므로
        # 15에서의 연산 횟수 +1과 기존 20의 연산 횟수를 비교하게 된다.
    return -1 if dp[y] == 1000001 else dp[y]

x, y, n = 10, 40, 5

print(solution(x, y, n))