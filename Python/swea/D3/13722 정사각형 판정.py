def check():
    start_y, start_x = 21, 21
    end_y, end_x = 0, 0

    for i in range(n):  # 좌측 상단 꼭짓점과 우측 하단 꼭짓점 위치 탐색, 주어진 판의 모든 #을 이용해야하므로 최소 위치와 최대 위치 탐색
        for j in range(n):
            if board[i][j] == '#':
                start_y, start_x = min(start_y, i), min(start_x, j)  # 좌측 상단 꼭짓점
                end_y, end_x = max(end_y, i), max(end_x, j)  # 우측 하단 꼭짓점

    if end_x - start_x != end_y - start_y:  # 가로 세로의 길이가 다르다면
        return 'no'

    for i in range(start_y, end_y + 1):  # 찾은 위치를 기준으로
        for j in range(start_x, end_x + 1):  # 사각형이 채워져있는지 확인
            if board[i][j] != '#':
                return 'no'
    return 'yes'  # 지금까지 어떠한 리턴이 없었다면

for t in range(1, int(input()) + 1):
    n = int(input())
    board = [input() for _ in range(n)]

    print(f'#{t} {check()}')