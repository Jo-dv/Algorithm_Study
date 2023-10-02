for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    plus = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    cross = [[-1, -1], [1, -1], [-1, 1], [1, 1]]

    for y in range(n):
        for x in range(n):
            plus_result, cross_result = grid[y][x], grid[y][x]
            for plus_d, cross_d in zip(plus, cross):
                for power in range(1, m):
                    plus_y, plus_x = y + plus_d[0] * power, x + plus_d[1] * power
                    cross_y, cross_x = y + cross_d[0] * power, x + cross_d[1] * power
                    if -1 < plus_y < n and -1 < plus_x < n:
                        plus_result += grid[plus_y][plus_x]
                    if -1 < cross_y < n and -1 < cross_x < n:
                        cross_result += grid[cross_y][cross_x]
                answer = max(answer, plus_result, cross_result)

    print(f'#{t} {answer}')