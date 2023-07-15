T = int(input())

for i in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    A = P * W  # L당 요금
    if W <= R:
        B = Q
    else:
        B = Q + (W - R) * S  # 기본 사용량: Q + 초과량에 한 해, A사와 동일하게 책정되는 금액: (W - R) * S

    print(f'#{i} {min(A, B)}')