note_length = int(input())
note = input()
direction = {0: (-1, 0), 1: (0, -1), 2: (1, 0), 3: (0, 1)}  # 북서남동 순, 회전시 연결되는 방향 순으로 생성, 인덱스는 0부터
y, x, d = 0, 0, 2  # 초기 임의의 시작지점, 방향은 남 고정
mask = [(y, x)]  # 이동한 좌표를 저장할 리스트

for i in note:
    if i == 'L':  # 왼쪽이라면
        d = (d + 1) % 4  # 0123에서 1230으로 매핑 가능, 0이 왼쪽에서 오른쪽으로
    elif i == 'R':  # 오른쪽이라면
        d = (d + 7) % 4  # 0123에서 3012로 매핑 가능, 3이 오른쪽에서 왼쪽으로
    else:
        my, mx = direction[d]  # 방향에 따라
        y += my
        x += mx
        mask.append((y, x))  # 이동한 좌표 저장

row = max(mask)[0] - min(mask)[0] + 1  # y축의 길이
col = max(mask, key=lambda idx: idx[1])[1] - min(mask, key=lambda idx: idx[1])[1] + 1  # x축의 길이
maps = [['#'] * col for _ in range(row)]  # 계산한 축의 길이를 바탕으로 맵 생성, 전부 벽으로 초기화
min_y, min_x = min(mask, key=lambda idx: idx[0])[0], min(mask, key=lambda idx: idx[1])[1]
# 시작점을 고정하기 위해 음수값을 제거하기 위한 값 저장, 가령 x축으로 -1이라면 최소 좌측보단 우측에서 이동했다고 볼 수 있음

for i in mask:  # 해당 문제는 일단 좌표를 상대기준으로 보고 일단 그림을 따라 그려봄, 그럼 시작위치 파악 가능하고 그에 맞춰 값 보정식 생각 가능
    cy, cx = i  # 좌표들을 가져와서
    cy += abs(min_y)  # 보정 값으로 매핑, 생성한 맵의 좌표상 음수는 존재할 수 없으므로 절대값 사용(음수가 되면 인덱스가 거꾸로 탐색됨)
    cx += abs(min_x)
    if maps[cy][cx] == '#':  # 해당 좌표가 벽이라면
        maps[cy][cx] = '.'  # 벽이 아닌 길로 간주

for i in maps:
    print(''.join(i))  # 출력 형식에 맞춰서
    