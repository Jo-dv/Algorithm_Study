T = int(input())

for i in range(1, T+1):
    N = int(input())

    matrix = [[j for j in map(int, input().split())] for _ in range(N)]

    print(f'#{i}')  # matrix가 주어졌을 때, 회전한 모습을 보고 단순 index 조작만 수행하면 됨
    for j in range(len(matrix)):  # 90
        for k in range(1, len(matrix) + 1):
            print(matrix[-k][j], end='')
        print(end=' ')
        for k in range(1, len(matrix) + 1):  # 180
            print(matrix[-j - 1][-k], end='')
        print(end=' ')
        for k in range(len(matrix)):  # 270
            print(matrix[k][-j - 1], end='')
        print()