code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
        '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

T = int(input())

for i in range(1, T + 1):
    N, M = map(int, input().split())
    case = [list(input()) for _ in range(N)]
    res = []
    col, row = 0, 0

    for j, k in enumerate(case):  # 암호가 있는 라인을 탐색
        if sum(map(int, k)) == 0:  # 한 라인의 합이 0이라면 암호가 없는 라인
            continue
        row = j
        break

    for j in range(M-1, -1, -1):  # 암호가 있는 구간을 탐색
        if case[row][j] == '1':  # 모든 암호의 비트의 끝자리는 항상 1이므로 역으로 탐색
            col = j-55  # 비트의 길이는 56이므로 마지막 구간 -56 + 1(시작 지점으 비트)
            break

    for j in range(0, 56, 7):  # 7비트씩 끊어서
        res.append(code[''.join(case[row][col+j:col+j+7])])  # 해당 비트들에 부합하는 값을 추가

    if (sum([k for j, k in enumerate(res) if j % 2 == 0])*3 + sum([k for j, k in enumerate(res) if j % 2 != 0])) % 10 == 0:
        print(f'#{i} {sum(res)}')
    else:
        print(f'#{i} {0}')