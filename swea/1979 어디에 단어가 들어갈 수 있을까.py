T = int(input())

for i in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]  # 행을 기준
    t_puzzle = [list(i) for i in zip(*puzzle)]  # 전치 행렬, 열을 기준
    store = []

    for r_line, c_line in zip(puzzle, t_puzzle):  # 한 줄씩
        row_check, col_check = 0, 0
        for row, col in zip(r_line, c_line):  # 한 칸씩
            if row == 1:  # 해당 칸이 빈 공간이라면
                row_check += 1
            else:  # 빈 공간이 아니라면
                store.append(row_check)  # 지금까지 확인한 빈 공간의 길이를 저장, 즉 연속된 빈 공간의 길이를 저장하는 것
                row_check = 0  # 이후 초기화, 끊긴 시점에서 다시 빈 공간이 나오면 처음부터 다시 길이를 재야함
            if col == 1:
                col_check += 1
            else:
                store.append(col_check)
                col_check = 0
        else:  # 탐색이 끝났을 때 마지막 빈 공간의 길이를 저장
            store.append(row_check)
            store.append(col_check)

    store = [i for i in store if i == K]  # 길이를 저장한 list에서 K 길이의 빈 공간이 있는지 확인
    print(f'#{i} {len(store)}')
