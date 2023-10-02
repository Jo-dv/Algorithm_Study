t = int(input())

for _ in range(t):
    cmds = input()
    d = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 이동 방향 벡터
    face = 0  # 마주한 방향, 이동 벡터의 순서에 따름
    x, y = 0, 0  # 초기 좌표
    trace = [(x, y)]  # 거북이가 지나간 영역의 넓이를 구하기 위해 이동한 좌표들을 저장할 리스트

    for cmd in cmds:  # 명령어들 중
        if cmd == 'L':  # 0 1 2 3 -> 1 2 3 0
            face = (face + 1) % 4
        elif cmd == 'R':  # 0 1 2 3 -> 3 0 1 2
            face = (face + 3) % 4
        else:
            dx, dy = d[face]
            if cmd == 'F':  # 앞
                x += dx
                y += dy
            else:  # 뒤
                x -= dx
                y -= dy
            trace.append((x, y))  # 계산된 좌표 저장

    x1, y1 = min(trace, key=lambda i: i[0])[0], max(trace, key=lambda i: i[1])[1]  # 사각형의 좌측 상단
    x2, y2 = max(trace, key=lambda i: i[0])[0], min(trace, key=lambda i: i[1])[1]  # 사각형의 우측 하단
    print((x2 - x1) * (y1 - y2))  # 가로 * 세로, 양의 방향(최대)에서 음으 방향으로 계산(최소)
