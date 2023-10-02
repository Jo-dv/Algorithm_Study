from collections import deque

m, n = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
answer = 0

q = deque([])
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for y in range(n):
    for x in range(m):
        if maps[y][x] == 1:  # 시작 지점이 한 곳이 아니기 때문에 전부 저장
            q.append((y, x))

while q:
    cy, cx = q.popleft()
    for i in d:
        my = cy + i[0]
        mx = cx + i[1]
        if 0 <= mx < m and 0 <= my < n and maps[my][mx] == 0:  # 범위를 벗어나지 않고 익지 않은 토마토라면
            maps[my][mx] = maps[cy][cx] + 1  # 이전 토마토 일수에서 누적
            q.append((my, mx))  # 해당 지점 탐색 지점으로 지정

for i in maps:  # 이후 순회하면서
    if 0 in i:  # 익지 않은 토마토가 있다면
        print(-1)
        break  # 반복 종료
    answer = max(max(i), answer)  # 그렇지 않으면 큰 값이 나올 때마다 갱신, i는 리스트이므로 i 자체에 max를 취해줘야 함
else:
    print(answer - 1)  # 일수 = 시작지점으로 했으므로 1부터 시작, 하지만 0부터 카운팅해야 하므로 1을 빼줌
