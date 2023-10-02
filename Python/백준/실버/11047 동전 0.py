n, k = map(int, input().split())
a = [int(input()) for i in range(n)]
idx, answer = -1, 0

while k > 0:  # 기본적인 그리디 문제, 만들 돈이 0이 될 때까지
    if a[idx] > k:  # 금액이 큰 순부터
        idx -= 1  # 현재 금액이 만들어야 할 금액보다 클 경우 다음 금액으로 이동
        continue
    answer += k // a[idx]  # 몫으로 필요한 동전의 수를 구함
    k %= a[idx]  # 남은 돈으로 갱신


print(answer)