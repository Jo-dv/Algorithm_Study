T = int(input())

days = {'MON': 1, 'TUE': 2, 'WED': 3, 'THU': 4, 'FRI': 5, 'SAT': 6, 'SUN': 14}  # 일요일일 경우

for i in range(1, T+1):
    print(f'#{i}', abs(7-days[input()]))  # 7을 기준으로 차이나는 만큼이 다음 일요일까지 남은 기간, 일요일일 경우 음수가 나오므로 abs