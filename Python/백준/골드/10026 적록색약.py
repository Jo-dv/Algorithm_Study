import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 때문에 틀림, 데이터 제한 확인할 것, 입력 최대 100으로 100 x 100 그리드 생성 가능

n = int(input())
maps = [input() for _ in range(n)]
a = [0, 0, 0, 0]
flag = 0

def dfs(y, x, target, flag=0):
    if 0 <= y < n and 0 <= x < n:  # 범위를 위배하지 않은 경우
        cond = maps[y][x] == target if not flag else maps[y][x] != target  # 플래그에 따라 적녹색약 탐색의 타겟을 달리함
        if cond and not visited[y][x]:  # 플래그에 따라 원하는 타켓이면서 아직 방문하지 않았다면
            visited[y][x] = True
            dfs(y - 1, x, target, flag)
            dfs(y + 1, x, target, flag)
            dfs(y, x - 1, target, flag)
            dfs(y, x + 1, target, flag)
            return True
    return False


visited = [[False] * n for _ in range(n)]  # visited가 False부분만 탐색하므로 RGB의 경우 순차적으로 탐색하면 됨
for i, t in enumerate(['R', 'G', 'B', 'B']):
    if i == 3:  # 적녹색약을 탐색해야 될 경우
        visited = [[False] * n for _ in range(n)]  # 다시 생성
        flag = 1  # 플래그 활성화
    for r in range(n):
        for c in range(n):
            if dfs(r, c, t, flag):
                a[i] += 1


print(sum(a[:3]), sum(a[2:]))