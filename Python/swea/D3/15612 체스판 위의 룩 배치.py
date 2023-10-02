def check1():  # 위치가 위배되지 않는지 확인
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 행, 열 이동

    for i in range(8):  # 모든 경우에 대해서
        for j in range(8):
            if board[i][j] == 'O':  # 시작 위치 탐색
                for dy, dx in direction:  # 모든 방향에 대해서
                    my, mx = i + dy, j + dx
                    while 0 <= my < 8 and 0 <= mx < 8:  # 범위가 위배되지 않고
                        if board[my][mx] == 'O':  # 동선이 겹칠 경우
                            return False
                        my += dy  # 방향 갱신
                        mx += dx

    return True  # 이상이 없다면 True 반환


def check2():  # 숫자에서 위배되지 않는지 확인
    count = 0

    for i in range(8):  # 모든 행에 대해
        count += board[i].count('O')  # 해당 행에 룩 카운팅 후, 누적

    return True if count == 8 else False  # 카운팅 결과 8이면 이상 없음 아니라면 이상 있음


for t in range(1, int(input()) + 1):
    board = [input() for _ in range(8)]
    answer = 'yes' if check1() and check2() else 'no'  # 모든 조건에 이상이 없으면 yes 아니라면 no
    print(f'#{t} {answer}')

