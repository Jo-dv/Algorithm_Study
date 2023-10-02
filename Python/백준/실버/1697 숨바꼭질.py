from collections import deque

def bfs(d, n, k):
    q = deque([n])

    while q:
        cur = q.popleft()
        if cur == k:  # 현재 시작 위치가 목적지라면
            return d[cur]  # 해당 목적지에 걸린 시간을 반환
        for i in [cur-1, cur+1, cur*2]:  # 세 가지 경우에 대해
            if 0 <= i <= 100000 and not d[i]:  # 탐색할 위치가 범위를 벗어나지 않고 아직 방문하지 않았다면
                d[i] = d[cur] + 1  # 방문할 위치에 현재 시간 + 1을 저장
                q.append(i)  # 해당 위치부터 탐색하기 위해 큐에 저장

n, k = map(int, input().split())
d = [0] * 100001  # 무한 루프를 방지 및 최저 시간을 저장하는 리스트 생성, 다시 방문하게 되면 해당 지점에 최저 시간 방문이 아니게 됨으로 재방문 방지
print(bfs(d, n, k))