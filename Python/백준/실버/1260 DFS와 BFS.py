from collections import deque

n, m, v = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
for i in range(m):  # 양방향 그래프 초기화
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in graph:
    graph[i].sort()  # 번호가 적은 순으로 방문

visited = [False] * (n + 1)  # 노드 번호가 1부터 시작하므로 임의의 노드 0 생성
answer_dfs, answer_bfs = [], []


def dfs(s, visit):
    visit[s] = True
    answer_dfs.append(s)

    for i in graph[s]:
        if not visit[i]:
            dfs(i, visit)


def bfs(s, visit):
    q = deque([s])  # deque는 iterable한 객체로 초기화 가능, 숫자 단일을 집어넣어서 초기화 할 수는 없음, deque([]) 형태 초기화가 맘 편함
    visit[s] = True

    while q:
        node = q.popleft()
        answer_bfs.append(node)

        for i in graph[node]:
            if not visit[i]:
                q.append(i)
                visit[i] = True


dfs(v, visited.copy())
bfs(v, visited.copy())

print(*answer_dfs)
print(*answer_bfs)