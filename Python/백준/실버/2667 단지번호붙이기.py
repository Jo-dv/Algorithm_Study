'''
def dfs(y, x):
    global count

    if 0 <= y < n and 0 <= x < n and maps[y][x] and not visited[y][x]:  # 유효범위이며 집이 있고 아직 방문하지 않았다면
        visited[y][x] = True  # 방문 처리
        count += 1  # 가구 수 갱신
        dfs(y - 1, x)
        dfs(y + 1, x)
        dfs(y, x - 1)
        dfs(y, x + 1)
        return True  # 모든 탐색 종료 후 True 반환
    return False  # 위 조건에 하나라도 부합하지 않으면 탐색 실패


n = int(input())
maps = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
counts = []
count, town = 0, 0

for i in range(n):
    for j in range(n):
        if dfs(i, j):  # 단지를 발견할 때 마다
            town += 1  # 단지 수 갱신
            counts.append(count)  # 단지의 가구 수 저장
            count = 0  # 처리가 끝나면 가구 수 초기화

print(town)
for i in sorted(counts):
    print(i)'''

from collections import deque

def bfs(y, x):
    q = deque([(y, x)])
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    count = 1  # 1일 때 함수가 실행되므로 1부터 계산함

    maps[y][x] = 0  # 시작 부분 탐색 완료 처리

    while q:
        y, x = q.popleft()
        for dy, dx in d:
            my, mx = y + dy, x + dx
            if 0 <= my < n and 0 <= mx < n and maps[my][mx] == 1:  # 범위를 벗어나지 않고 탐색하지 않았다면
                maps[my][mx] = 0  # 이동한 곳 탐색 완료 처리
                q.append((my, mx))  # 이동한 좌표 저장
                count += 1  # 가구 수 갱신

    return count


n = int(input())
maps = [list(map(int, input())) for _ in range(n)]
town = 0
counts = []

for i in range(n):
    for j in range(n):
        if maps[i][j]:
            counts.append(bfs(i, j))
            town += 1

print(town)
for i in sorted(counts):
    print(i)