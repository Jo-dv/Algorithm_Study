n, m = map(int, input().split())
y, x, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 문제에서 제시한 이동 방향
answer = 0

while True:
    if maps[y][x] == 0:  # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
        maps[y][x] = -1  # 청소 했다는 표시
        answer += 1  # 청소한 구역의 수 갱신
    elif maps[y + 1][x] != 0 and maps[y - 1][x] != 0 and maps[y][x - 1] != 0 and maps[y][x + 1] != 0:
        # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우(벽 포함)
        my, mx = direction[d]  # 이동 방향
        if maps[y - my][x - mx] == -1:  # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
            y -= my
            x -= mx
        else:  # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
            break
    else:  # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
        d = 3 if d - 1 < 0 else d - 1  # 1. 반시계 방향으로 90도 회전
        my, mx = direction[d]
        if maps[y + my][x + mx] == 0:  # 2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
            y += my
            x += mx

print(answer)