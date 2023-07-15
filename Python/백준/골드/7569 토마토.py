from collections import deque

m, n, h = map(int, input().split())  # 열, 행, 높이
maps = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]  # 3차원 맵 입력
q = deque()
d = [(-1, 0, 0), (1, 0, 0), (0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0)]  # 위아래좌우상하
flag, answer = 0, 0

for z in range(h):
    for y in range(n):
        for x in range(m):
            if maps[z][y][x] == 1:  # 조건문 특성상 1 = True, 0 = False로 보는게 아니라 0을 제외한 나머지를 전부 True로 봄
                # 처음에 if maps[z][y][x]로 해서 계속 해맸음, 이 부분이 틀릴거라 생각지도 못해서 계속 로직만 들여다 보면서 시간 낭비
                q.append((z, y, x))  # 맵들을 모두 순회하면서 토마토가 있는 부분에 좌표 저장

while q:
    z, y, x = q.popleft()

    for i in d:  # 현재 좌표에서 방향 갱신
        mz = z + i[0]
        my = y + i[1]
        mx = x + i[2]
        if 0 <= mz < h and 0 <= my < n and 0 <= mx < m and maps[mz][my][mx] == 0:  # 범위를 벗어나지 않고 일반 토마토라면
            maps[mz][my][mx] = maps[z][y][x] + 1
            q.append((mz, my, mx))

for i in maps:  # 각 층을 가져와서
    if not flag:  # 플래그에 문제가 없다면
        for j in i:  # 각 층의 행을 가져와서
            if 0 in j:  # 해당 행에 익지 않은 토마토가 있다면
                print(-1)
                flag = 1  # 플래그 변경 후
                break  # 해당 반복 종료
            answer = max(answer, max(j))  # 현재 값과 해당 행의 최대값을 비교해 항상 최댓값을 가지도록 갱신
    else:
        break  # 플래그에 문제가 있을 경우 최종 반복 종료
if not flag:  # 반복이 종료된 후 플래그에 문제가 없다면
    print(answer-1)  # 토마토 값이 1이고 이것으로 시작하면서 값을 갱신했기 때문에 -1

