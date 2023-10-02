from collections import deque

g = [
    [],
    [2, 3],
    [1, 3, 4],
    [1, 2, 4],
    [2, 3, 5],
    [3, 4]
]
v = [False]*len(g)

def bfs(g, s, v):
    q = deque([s])
    v[s] = True

    while q:
        n = q.popleft()
        print(n, end=' ')

        for i in g[n]:
            if not v[i]:
                q.append(i)
                v[i] = True

bfs(g, 5, v)