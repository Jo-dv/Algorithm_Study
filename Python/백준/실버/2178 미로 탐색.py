from collections import deque

n, m = map(int, input().split())  # n: y, m: x
maze = [list(map(int, list(input()))) for _ in range(n)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 좌표 오타는 없는지 중복은 없는지 항상 확인할 것
q = deque([(0, 0)])  # 초기화 형태 유의할 것, 시작 위츠는 (1, 1) 좌표상으로 (0, 0)으로 일반적인 리스트 좌표를 따름

while q:
    y, x = q.popleft()

    for i in d:
        my = y + i[0]
        mx = x + i[1]
        if 0 <= my < n and 0 <= mx < m and maze[my][mx] == 1:  # 좌표가 유효하고 해당 지역이 탐색하지 않은 곳이라면
            maze[my][mx] = maze[y][x] + 1  # 갱신
            q.append((my, mx))  # 해당 좌표를 탐색하기 위해 저장

print(maze[-1][-1])