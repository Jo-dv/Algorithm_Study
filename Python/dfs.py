g = [
    [],
    [2, 3],
    [1, 3, 4],
    [1, 2, 4],
    [2, 3, 5],
    [3, 4]
]
v = [False]*len(g)

def dfs(g, s, v):
    v[s] = True
    print(s, end=' ')

    for i in g[s]:
        if not v[i]:
            dfs(g, i, v)

dfs(g, 5, v)