for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    answer = 0

    plus = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 스프레이 방향 벡터
    cross = [[-1, -1], [1, -1], [-1, 1], [1, 1]]

    for y in range(n):  # 탐색의 방향은 왼쪽에서 오른쪽, 위에서 아래로 진행
        for x in range(n):
            plus_result, cross_result = grid[y][x], grid[y][x]  # 스프레이 형태: 십자, 엑스자 시작 값
            for plus_d, cross_d in zip(plus, cross):  # 스프레이 방향 벡터 값을 하나씩 가져와서
                for power in range(1, m):  # 시작 값은 위에서부터 받았기 때문에 1 ~ m-1
                    plus_y, plus_x = y + plus_d[0] * power, x + plus_d[1] * power  # 해당 위치에 스프레이의 세기를 1씩 증가
                    cross_y, cross_x = y + cross_d[0] * power, x + cross_d[1] * power
                    if -1 < plus_y < n and -1 < plus_x < n:  # 증가된 스프레이의 값이 범위를 벗어나지 않은 경우
                        plus_result += grid[plus_y][plus_x]  # 해당 위치에 파리 값 합산
                    if -1 < cross_y < n and -1 < cross_x < n:
                        cross_result += grid[cross_y][cross_x]
                answer = max(answer, plus_result, cross_result)  # 반환할 값을 가장 큰 값으로 갱신

    print(f'#{t} {answer}')
