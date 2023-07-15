from collections import deque

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
answer = []
q = deque([])
visited = None

for _ in range(m):  # 양방향 그래프 초기화
    s, e = map(int, input().split())
    g[s].append(e)
    g[e].append(s)

for i in range(1, n + 1):  # 모든 노드 탐색
    visited = [0] * (n + 1)  # 해당 노드를 기준으로 할 때마다 새롭게 탐색하므로 visited 초기화
    q.append(i)  # 해당 노드를 시작 노드로

    while q:
        start = q.popleft()
        for node in g[start]:  # 시작 노드와 연결된 노드들을 가져와서
            if not visited[node]:  # 방문하지 않았다면(=0), 노드가 거쳐갔다면 0이 아닌 거쳐간 횟수가 저장됨
                visited[node] = visited[start] + 1  # 해당 노드는 자기와 연결된 시작 노드의 횟수 + 1
                q.append(node)  # 이후 탐색을 위해 해당 노드 저장
    answer.append(sum(visited[1:i] + visited[i+1:]))  # 모든 탐색이 끝나면 원래의 시작 노드를 제외한 노드들의 거쳐간 횟수를 합산

print(answer.index(min(answer)) + 1)  # 합산 결과 중 값이 가장 적은 노드의 번호 출력, answer는 인덱스가 0부터 시작하므로 + 1