def dfs(s, d):
    global answer
    v[s] = True  # 해당 노드는 방문

    if answer < d:  # 지금 방문한 노드의 수가 현재 기록한 노드의 수보다 많은면
        answer = d  # 갱신, d는 지역 변수이므로 노드의 분기점이 3개있고 d가 2라면 세 분기를 전부 2라는 깊이를 가지고 탐색하는 것

    for i in maps[s]:  # 해당 노드와 연결된 노드들에 대해서
        if not v[i]:  # 방문하지 않았다면
            dfs(i, d + 1)  # 방문한 노드를 늘려 마저 탐색
            v[i] = False  # 탐색이 종료되면 다시 분기로 돌아와서 나머지 부분을 탐색하기 위해 방문 취소 처리
            # 가령 하나의 분기를 가지는 그래프에서 첫 번째 경로는 깊이가 3, 나머지 경로의 깊이가 4라면 False 처리해서 돌아오지 않을 경우
            # 오답이 됨, 즉 분기에 대해 모든 경로를 탐색하기 위해 하는 처리임


for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    maps = [[] for _ in range(n+1)]  # 0번에 해당하는 더미 노드를 가진 그래프 생성
    for _ in range(m):  # 무방향 그래프 초기화
        s, e = map(int, input().split())
        maps[s].append(e)
        maps[e].append(s)

    answer = 1  # 무조건 하나의 노드는 방문하게 됨

    for i in range(1, n):  # 각 노드에 대해서 탐색
        v = [False] * (n + 1)  # 어떤 노드에서 탐색하냐에 따라 경로가 달라지므로
        dfs(i, 1)  # 1은 answer와 같은 의미로 새로운 노드로 탐색할 때마다 1로 초기화되어야 함

    print(f'#{t} {answer}')