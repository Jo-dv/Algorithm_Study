for t in range(1, int(input())+1):
    n = int(input())
    grid = [[0] * n for _ in range(n)]
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 주어진 문제대로 우 하 좌 상 순으로 방향 배치
    y, x = 0, -1  # 초기 위치
    num = 1

    while num != n**2 + 1:  # + 1을 하지 않으면 아래 코드상 마지막 장소를 방문하지 않게 됨
        for dy, dx in direction:  # 네 방향을 순회하며
            my, mx = y + dy, x + dx  # 탐색 시작 위치 초기화
            while 0 <= my < n and 0 <= mx < n:  # 범위가 유효하다면
                if grid[my][mx] == 0:  # 그리고 아직 방문하지 않았다면
                    grid[my][mx] = num  # 방분
                    num += 1  # 다음 방문을 위해 값 갱신
                    y, x = my, mx  # 마지막 방문 위치 갱신
                my += dy  # 탐색 위치 갱신
                mx += dx

    print(f'#{t}')
    for i in grid:
        print(*i)

'''
20221024 작성 코드
T = int(input())

def cord_update(y, x, dir=1):
    cord = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # (y, x)의 형태, 틀을 다 채울 때까지 해당 좌표들을 반복
    return y + dir * cord[direction][0], x + dir * cord[direction][1]

for i in range(1, T+1):
    N = int(input())
    ans = [[0]*N for _ in range(N)]
    y, x, direction = 0, 0, 0  # 초기 y 좌표, x 좌표, 방향

    for j in range(1, N**2+1):  # 달팽이 크기만큼
        if x < 0 or y < 0 or x == N or y == N or ans[y][x] != 0:  # 갱신된 좌표가 틀을 벗어나거나 이미 채워졌다면
            y, x = cord_update(y, x, -1)  # 이전 좌표로 복귀
            if direction == 3:  # 마지막 방향이라면 초기 방향으로 복귀
                direction = 0
            else:
                direction += 1  # 아닐 경우, 다음 방향으로 갱신
            y, x = cord_update(y, x)  # 방향에 따른 다음 좌표로 갱신

        ans[y][x] = j  # 좌표에 따라 값 갱신
        y, x = cord_update(y, x)  # 좌표 갱신

    print(f'#{i}')
    for j in ans:
        print(*j)
'''