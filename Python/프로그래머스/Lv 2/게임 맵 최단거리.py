from collections import deque

def solution(maps):
    q = deque([(0, 0)])  # 시작 위치 (y, x)
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우

    while q:  # BFS
        y, x = q.popleft()
        for i in direction:  # 상하좌우로 이동하여 탐색
            my = y + i[0]
            mx = x + i[1]
            if my < 0 or len(maps) <= my or mx < 0 or len(maps[0]) <= mx or maps[my][mx] == 0:
                continue  # 끝에 도달했거나 인덱스 범위를 초과했거나 갈 수 없는 곳이라면 다음 구역 탐색
            if maps[my][mx] == 1:  # 이동한 곳이 처음온 길이라면
                maps[my][mx] = maps[y][x] + 1  # 해당 지점으로 이동하기 전 이동 거리와 합산
                q.append((my, mx))  # 이동한 곳부터 다시 탐색

    return -1 if maps[-1][-1] == 1 else maps[-1][-1]
    # 목적지는 고정이므로 값이 1이라면 갈 수 없다는 의미, 문제 조건에서 1x1 크기는 없다고 했기 때문

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

print(solution(maps))