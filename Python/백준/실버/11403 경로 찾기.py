n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]  # 플로이드 워셜: 행은 시작 노드, 열은 도착 노드

for i in range(n):  # 인터체인지 노드
    for s in range(n):  # 시작 노드
        for e in range(n):  # 도착 노드
            if g[s][i] == g[i][e] == 1:  # 시작 -> 인터체인지, 인터체인지 -> 도착이 일치한다면 = 연결되어 있다면
                g[s][e] = 1  # 직통으로 이동 가능하다고 간주

for i in g:
    print(*i)