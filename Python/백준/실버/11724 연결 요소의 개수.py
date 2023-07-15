import sys
sys.setrecursionlimit(10**9)  # 10**10으로 하니 오버플로우 발생, 자체를 설정하지 않으면 런타임 에러 발생

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):  # 양방향 그래프 생성
    s, e = map(int, sys.stdin.readline().split())
    g[s].append(e)
    g[e].append(s)

answer = 0

def dfs(node):
    visited[node] = True

    for i in g[node]:  # 해당 노드를 기준으로
        if not visited[i]:  # 방문하지 않았다면
            dfs(i)  # 탐색시작

for i in range(1, n + 1):  # 노드를 전부 순회하면서
    if not visited[i]:
        dfs(i)  # i번째 노드를 기준으로 탐색이 끝났다면
        answer += 1  # 연결된 그래프의 수 갱신

print(answer)