from collections import deque

def bfs(s, maps, target):
    q = deque([s])
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cmaps = [[-1 if maps[i][j] == 'X' else 0 for j in range(len(maps[0]))] for i in range(len(maps))]
    # 벽과 벽이 아닌 부분을 -1과 0으로 표현

    while q:
        y, x = q.popleft()
        for i in direction:
            my = y + i[0]
            mx = x + i[1]
            if my < 0 or len(maps) <= my or mx < 0 or len(maps[0]) <= mx or maps[my][mx] == 'X':
                continue  # 움직일 수 없는 곳이라면
            if cmaps[my][mx] == 0:  # 이동한 곳이 탐색하지 않은 곳이라면
                cmaps[my][mx] = cmaps[y][x] + 1  # 이동을 했기 때문에 해당 지점에 대한 방문 시간을 갱신
                if maps[my][mx] == target:  # 또한 이동한 곳이 찾고자 한 곳이라면
                    return (my, mx), cmaps[my][mx]  # 해당 지점의 좌표와 시간 반환
                q.append((my, mx))  # 아니라면 해당 지점부터 다시 탐색해야 하므로 큐에 저장
    return False  # 좌표가 반환되지 않았다면 도달할 수 없는 곳이므로 False 반환

def solution(maps):
    s = None
    for y in range(len(maps)):  # 시작 지점 탐색
        if 'S' in maps[y]:
            s = (y, maps[y].index('S'))
            break

    lever = bfs(s, maps, 'L')  # 레버 위치 탐색
    if lever:  # 레버를 찾았다면
        exit = bfs(lever[0], maps, 'E')  # 레버 위치에서부터 출구 탐색
        return lever[-1] + exit[-1] if exit else -1  # 레버와 출구 모두 찾았다면 총 시간 반환, 출구를 찾지 못했다면 -1
    else:
        return -1  # 레버를 찾지 못했다면

    # 해당 문제는 최종 목적지를 찾기 위해 선행 조건이 완료되어야 하며 그 조건에서 이미 왔던 곳도 다시 방문할 수 있기에, 한 번에 해결하려면
    # 이동 거리가 커질수록 탐색이 오래걸리게 됨
    # 그렇기에 선행 조건과 최종 조건을 각각 나눠서 탐색하고 그 결과를 합산

maps = ["SOOEL","XXXXO","OOOOO","OXXXX","OOOOO"]
print(solution(maps))