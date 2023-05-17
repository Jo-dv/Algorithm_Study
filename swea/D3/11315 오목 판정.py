def check_stones():
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]  # 모든 방향

    for i in range(n):
        for j in range(n):
            if board[i][j] == 'o':  # 시작할 위치
                for dy, dx in directions:  # 모든 방향에 대해서
                    count = 1  # 시작할 위치에 돌이 있으므로 1부터 시작
                    ny, nx = i + dy, j + dx  # 이동할 방향
                    while 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 'o':  # 방향에 대해 유효성 검사
                        count += 1  # 개수 갱신
                        if count >= 5:  # 5이상이면 더 이상 탐색할 필요 없음
                            return True
                        ny += dy  # 이동
                        nx += dx
    return False  # 반복을 모두 돌았는데 리턴되지 않았다는 것은 찾지 못했다는 뜻


for t in range(1, int(input()) + 1):
    n = int(input())
    board = [input() for _ in range(n)]  # 바둑판 초기화
    answer = 'YES' if check_stones() else 'NO'
    print(f'#{t} {answer}')
