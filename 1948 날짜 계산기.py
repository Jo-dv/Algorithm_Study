import datetime

T = int(input())

for i in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())
    res = datetime.datetime(2022, m2, d2) - datetime.datetime(2022, m1, d1)

    print(f'#{i} {res.days+1}')