T = int(input())
calendar = {'01': '31', '03': '31', '05': '31', '07': '31', '08': '31', '10': '31', '12': '31',
            '04': '30', '06': '30', '09': '30', '11': '30',
            '02': '28'}  # 달력 정의

for i in range(1, T+1):
    ymd = input()
    y = ymd[:4]
    m = ymd[4:6]
    d = ymd[6:]
    if m in calendar.keys() and 1 <= int(d) <= int(calendar[m]):  # 연도는 고려대상이 아님 그저 네 자리면 됨
        print(f'#{i} {y}/{m}/{d}')  # m이 dictionary에 존재하고 d가 m을 key로 하는 value의 유효 범위 안에 있다면
    else:
        print(f'#{i} -1')