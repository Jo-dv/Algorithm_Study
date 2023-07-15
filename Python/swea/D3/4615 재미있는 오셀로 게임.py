for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    cmd = [tuple(map(int, input().split())) for _ in range(m)]  # 돌을 나두는 위치와 색상
    grid = [[0] * n for _ in range(n)]  # 게임판 생성
    grid[n // 2 - 1][n // 2] = grid[n // 2][n // 2 - 1] = 1  # 초기 돌 생성
    grid[n // 2 - 1][n // 2 - 1] = grid[n // 2][n // 2] = 2
    d = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]  # 상하좌우대각

    for c in cmd:  # 명령어를 하나씩 가져와서
        y, x, stone = c
        y, x = y - 1, x - 1  # 입력되는 좌표는 (1, 1)로 시작하므로 -1을 해서 생성한 게임판 인덱스의 맞춰줌
        grid[y][x] = stone  # 입력 받은 위치에 돌 배치

        for i in d:  # 총 8가지 방향에 대해 유효성 검사
            my = y + i[0]
            mx = x + i[1]
            flag = False  # 뒤집기 유효성 여부

            while 0 <= my < n and 0 <= mx < n:  # 이동하려는 범위가 게임판을 벗어나지 않고
                if not grid[my][mx]:  # 이동하려는 위치에 돌이 없다면
                    break  # 오셀로는 돌을 위치시킬 때 그 사이에 반드시 돌이 존재해야 하므로, 돌을 위치한 상태에서 0이 존재해서는 안됨
                if grid[my][mx] == stone:  # 처음에 둔 돌과 동일한 색상의 돌을 발견하면
                    flag = True  # 뒤집기 가능
                    break
                my += i[0]  # 뒤집을 수 있는 위치를 발견할 때까지 주어진 범위만큼 탐색
                mx += i[1]

            if flag:  # 뒤집기가 유효하다면
                while y != my or x != mx:  # my 혹은 mx가 원래 위치로 돌아올 때까지
                    grid[my][mx] = stone  # 그 사이에 있는 돌들을 뒤집음
                    my -= i[0]  # 역으로 추적
                    mx -= i[1]
                # and를 사용하면 둘 중 하나가 true가 되는 순간 조건 자체는 false가 됨.
                # 대각이면 상관없지만 수직 및 수평은 상시 y == my이거나, x == mx이기 때문에 바로 false가 돼서 뒤집을 수 없음

    b = sum(i.count(1) for i in grid)
    w = sum(i.count(2) for i in grid)

    print(f'#{t} {b} {w}')
