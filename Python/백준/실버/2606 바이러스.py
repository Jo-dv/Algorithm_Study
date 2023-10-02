n = int(input())
m = int(input())
network = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    s, e = map(int, input().split())  # 양방향 연결리스트
    network[s].append(e)
    network[e].append(s)


def dfs(s):
    visited[s] = True
    for i in network[s]:
        if not visited[i]:  # 요소로 리스트가 올 수 있다고 발생하는 경고, 하지만 리스트는 올 일이 없으므로 무시해도 됨
            dfs(i)


dfs(1)  # 1번이랑 연결된 부분만 탐색하면 됨
print(sum(visited) - 1)  # 1 자신도 포함시키므로 제외해줘야 함