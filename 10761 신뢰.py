for t in range(1, int(input()) + 1):
    case = list(input().split())
    N = int(case[0])
    o_pos, b_pos = 1, 1  # 초기 로봇들의 위치
    o_time, b_time = 0, 0  # 초기 로봇들의 작동 시간
    total_time = 0

    for i in range(1, N * 2, 2):
        cur = case[i:i + 2]  # 로봇과 버튼, ex) O2, B3, ...
        if cur[0] == 'O':  # 오렌지 로봇이라면
            distance = abs(int(cur[1]) - o_pos)  # 현재 로봇의 위치에서 다음 버튼까지의 거리, 뒤로도 이동할 수 있기 때문에 절대값을 취함
            total_time += 1 if distance <= total_time - o_time else (distance - (total_time - o_time) + 1)
            # 로봇이 이동할 거리가 전체 소요 시간에서 해당 로봇의 작동 시간의 차보다 작다면 다른 로봇이 움직일 때 이미 눌러야 하는 버튼의 위치에 도달했다는 의미이므로 버튼만 누름(1초 소요)
            # 도달은 이미 도달해서 대기한 것일 수도 있고 막 도착한 것일 수도 있음
            # 아니라면 현재 거리에서 남은 거리만큼 더 가서 버튼을 누름, (총 걸어야 하는 거리 - 현재 소요한 시간 + 버튼 누르는 시간), 버튼 1에 1초가 소요되므로
            # total time - robot time = 지금까지 전체 소요 시간에서 이전 시점까지의 로봇의 소요 시간의 차는 다른 로봇이 움직일 때 소요된 시간 의미
            # total이 4, o_time이 2라면 b로봇이 4만큼 시간을 소요할 때 o로봇은 2만큼의 시간을 썼다는 의미, 이것은 이동한 시간일 수도 있고 대기한 시간일 수도 있고 이동 및 대기의 시간일 수도 있다.
            o_pos = int(cur[1])  # 로봇의 위치 갱신
            o_time = total_time  # 로봇이 현재 위치까지 도달하여 행동을 마친 시점까지의 소요 시간
        else:
            distance = abs(int(cur[1]) - b_pos)
            total_time += 1 if distance <= total_time - b_time else (distance - (total_time - b_time) + 1)
            b_pos = int(cur[1])
            b_time = total_time

    print(f'#{t} {total_time}')
