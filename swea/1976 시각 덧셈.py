T = int(input())

for i in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())  # 시각 덧셈
    temp = divmod(m1 + m2, 60)  # 분의 합이 60 이상일 경우 그 차이만큼 시간에 더해주기 위해
    h, m = h1 + h2 + temp[0], temp[1]  # [0]은 몫 [1]은 나머지므로 차이만큼 시간에 더해짐
    if h > 12:  # 표현할 수 있는 시간은 1 ~ 12이므로 시간이 12보다 클 경우 12를 빼준다.
        h -= 12

    print(f'#{i} {h} {m}')
