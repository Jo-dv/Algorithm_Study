for t in range(1, int(input()) + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = -1

    dp = [1] * n  # 각 인덱스 기준 최장 길이를 가진 리스트 생성, 모든 값은 자기 자신을 가지므로 1이 됨

    for i in range(1, n):  # 1 ~ n-1 인덱스 기준으로
        for j in range(i):  # 처음부터 i번째 인덱스 앞까지 탐색하며
            if arr[j] < arr[i]:  # 탐색하는 값들이 기준 값보다 작으면
                dp[i] = max(dp[i], dp[j] + 1)  # i번째 값을 마지막으로 하는 최장 수열의 길이는 이전에 가장 긴 길이를 선택함
                # 예를 들어 [1, 3, 5]에서 i가 5일 경우 1을 기준으로 하면 2, 3을 기준으로 하면 3이 된다.
                answer = max(answer, dp[i])  # 갱신된 dp[i]가 answer보다 크면 해당 값으로 갱신

    print(f'#{t} {answer}')
