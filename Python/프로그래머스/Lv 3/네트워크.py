def solution(n, computers):
    answer = 0
    visited = [False] * n

    def dfs(i):
        visited[i] = True  # 방문 처리

        for j in range(n):  # 해당 컴퓨터와 연결된 컴퓨터들의 정보를 순회
            if not visited[j] and computers[i][j]:  # 순회된 컴퓨터 중에 아직 방문하지 않았고 현재 컴퓨터와 연결되었다면
                dfs(j)  # 해당 컴퓨터로 이동하여 그 쪽 컴퓨터와 어떤 컴퓨터가 연결되어 있는지 탐색

    for y in range(n):
        if not visited[y]:  # 해당 컴퓨터에 방문하지 않았다면
            dfs(y)
            answer += 1  # 연결 확인이 완료

    return answer


n, computers = 3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

print(solution(n, computers))