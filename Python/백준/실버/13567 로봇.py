m, n = map(int, input().split())
direction = {0: (1, 0), 1: (0, -1), 2: (-1, 0), 3: (0, 1)}  # 일반적인 좌표계 (0, 0) 시작 기준, 북은 위로 가야함
y, x, robot_direction = 0, 0, 3

for _ in range(n):
    cmd, d = input().split()
    if cmd == 'TURN':  # 방향 갱신
        robot_direction = (robot_direction + 7 if d == '1' else robot_direction + 1) % 4
    else:
        my, mx = direction[robot_direction]  # 방향에 따른 이동거리 갱신
        d = int(d)  # 이동할 거리
        if 0 <= x + mx * d < m and 0 <= y + my * d < m:  # 현재 좌표에서 이동할 거리가 범위를 벗어나지 않는다면
            x += (mx * d)
            y += (my * d)
        else:  # 벗어나면 반복 종료
            print(-1)
            break
else:
    print(x, y)  # 정상적으로 종료되었다면 최종 좌표 출력

