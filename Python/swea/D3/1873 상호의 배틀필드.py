t = int(input())

for i in range(1, t+1):
    h, w = map(int, input().split())
    maps = [list(input()) for _ in range(h)]
    n = int(input())
    cs = input()
    direction = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}  # 명령에 따른 탱크 이동 방향
    tank_direction = {'U': '^', 'D': 'v', 'L': '<', 'R': '>'}  # 명령에 따른 탱크 방향
    tank = ['^', 'v', '<', '>']  # 초기 탱크 방향 설정용 리스트
    y, x, d = 0, 0, None

    for col in range(h):
        for row in range(w):
            if maps[col][row] in tank:  # 탱크의 위치를 찾아서
                y, x = col, row  # 좌표 저장
                t = tank.index(maps[y][x])  # 탱크의 방향을 저장하기 위해 인덱스를 사용해서 모양 접근
                d = list(direction.values())[t]  # 모양에 따른(인덱스에 따른) 방향 설정

    for c in cs:
        if c != 'S':  # 발사 명령이 아니라면
            my, mx = d = direction[c]  # 현재 방향에 따른 이동 거리
            maps[y][x] = tank_direction[c]  # 일단 방향 변경
            if 0 <= y + my < h and 0 <= x + mx < w and maps[y + my][x + mx] == '.':  # 이동할 거리가 유효 범위이며 이동 가능이면
                maps[y + my][x + mx] = maps[y][x]  # 탱크 옮김
                maps[y][x] = '.'  # 탱크가 이동한 자리는 땅으로 변경
                y += my  # 탱크의 좌표 갱신
                x += mx
        else:
            my, mx = d  # 탱크의 방향에 따른 이동 거리
            sy, sx = y, x  # 미사일의 발사 위치
            while 0 <= sy + my < h and 0 <= sx + mx < w:  # 유효 범위 이내일 때가지 반복
                if maps[sy + my][sx + mx] == '#':  # 다만 철벽을 만나면 종료
                    break
                if maps[sy + my][sx + mx] == '*':  # 돌벽일 경우
                    maps[sy + my][sx + mx] = '.'  # 돌벽을 평지로 만든 후 종료
                    break
                sy += my  # 방향에 대한 거리만큼 이동
                sx += mx

    print(f'#{i} ', end='')
    for j in maps:
        print(''.join(j))