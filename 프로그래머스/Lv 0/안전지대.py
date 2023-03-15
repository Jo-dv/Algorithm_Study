board = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 1, 1, 0],
         [0, 0, 0, 0, 0]]

def extend(board):  # 인덱스 에러 방지를 위한 리스트 전처리
    length = len(board)  # 초기 리스트 길이 계산
    board.insert(0, [-1] * length)  # 해당 길이를 가진 가짜 리스트를 첫 행에 삽입
    board.append([-1] * length)  # 마지막 행에 삽입
    for i in board:  # 삽입돼서 변경된 길이에 맞춰
        i.insert(0, -1)  # 첫 열에 삽입
        i.append(-1)  # 마지막 열에 삽입

    return board

def solution(board):
    bd = extend(board)
    for i in range(1, len(bd)-1):  # 삽입된 값들을 제외하고
        if sum(bd[i][1:-1]) == 0:  # 해당 행의 총합이 0이 아니라면 다음으로
            continue
        for j in range(1, len(bd[i])-1):
            if bd[i][j] != 1:  # 1의 위치를 찾을 때까지 다음으로
                continue
            if not bd[i - 1][j]: bd[i - 1][j] = 1  # 상하좌우 값 변경
            if not bd[i + 1][j]: bd[i + 1][j] = 1
            if not bd[i][j - 1]: bd[i][j - 1] = 1
            if not bd[i][j + 1]: bd[i][j + 1] = 1
            if not bd[i - 1][j - 1]: bd[i - 1][j - 1] = 1  # 대각 값 변경
            if not bd[i - 1][j + 1]: bd[i - 1][j + 1] = 1
            if not bd[i + 1][j - 1]: bd[i + 1][j - 1] = 1
            if not bd[i + 1][j + 1]: bd[i + 1][j + 1] = 1

    return len([1 for i in range(1, len(bd)-1) for j in range(1, len(bd[i])-1) if bd[i][j] == 0])  # 0의 수 카운팅

'''
    n = len(board)
    danger = set()  # 집합 생성
    for i, row in enumerate(board):  # 행 탐색
        for j, x in enumerate(row):  # 열 탐색
            if not x:  # 열의 값이 1이 아니라면 다음으로
                continue
            danger.update((i+di, j+dj) for di in [-1, 0, 1] for dj in [-1, 0, 1])
            # 1의 위치를 기준으로, 상하좌우, 대각, 현재 위치 추가, 다음 탐색에서 겹치는 부분으로 중복된 좌표가 발생하면 집합 특성으로 제외
            # 탐색이 끝나면 집합에는 1의 영향을 받는 좌표들이 담겨있음
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)  # 범위를 벗어난 좌표를 제외하여 카운팅 후 전체 값에서 감산
'''
print(solution(board))