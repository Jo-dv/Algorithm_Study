T = int(input())

for i in range(1, T+1):
    case = list(input())
    grid = [['.']*(len(case)*4+1) for _ in range(5)]  # 생성되는 장식의 길이는 문자열의 길이 x 4 + 1

    for j in range(5):  # 행은 총 5
        for k in range(len(grid[0])):
            if j == 0 or j == 4:  # 첫 줄과 마지막 줄
                if k % 2 == 0 and k % 4 != 0:  # 짝수이되, 4의 배수가 아닐 경우, 2부터 4의 텀으로 #이 찍힘
                    grid[j][k] = '#'
            elif j == 2:  # 가운데 줄
                if k % 4 == 0:
                    grid[j][k] = '#'
                elif k % 2 == 0 and k % 4 != 0:  # 짝수이되, 4의 배수가 아닐 경우, 2부터 4의 텀으로 문자열이 찍힘
                    grid[j][k] = case.pop(0)
            else:  # 둘째 줄과 네번째 줄
                if k % 2 != 0:
                    grid[j][k] = '#'
    for j in grid:
        print(''.join(j))