import sys
sys.setrecursionlimit(10**4)  # 백준 재귀 최대 깊이는 1000이므로 해당 문제 최대 2500인 경우 런타임에러 발생

t = int(input())


def dfs(y, x):
    if x <= -1 or x > m-1 or y <= -1 or y > n-1:  # 탐색 범위를 벗어났다면
        return False
    if maps[y][x] == -1:  # 배추 발견, 상하좌우 탐색
        maps[y][x] *= -1  # 탐색된 곳은 반대 값을 취해줌으로써 1로 바꿔줌
        dfs(y - 1, x)
        dfs(y + 1, x)
        dfs(y, x - 1)
        dfs(y, x + 1)
        return True  # 탐색 종료
    return False  # 탐색할 곳이 없다면


for _ in range(t):
    m, n, k = map(int, input().split())
    maps = [[0] * m for _ in range(n)]
    answer = 0
    for _ in range(k):  # 좌표에 맞춰 배추 생성
        x, y = map(int, input().split())
        maps[y][x] = -1

    for i in range(n):
        for j in range(m):
            if dfs(i, j):  # 탐색 성공일 경우
                answer += 1

    print(answer)
