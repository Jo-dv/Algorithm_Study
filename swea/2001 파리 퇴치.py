T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())

    best_kill = -1
    fly = [list(map(int, input().split())) for _ in range(N)]  # matrix 형태로 문제 초기화

    size = N - M + 1  # 파리채의 계산 횟수
    for row_stride in range(size):  # 하단 이동을 위한 step의 size
        for col_stride in range(size):  # 우측 이동을 위한 step의 size
            kill = 0  # 파리채가 이동할 때 마다 잡은 파리수 초기화
            for row in range(M):  # 행을 모두 계산 후 파리채를 우측으로 이동하며 우측의 이동이 끝나면 하단으로 옮겨 다시 반복
                kill += sum(fly[row+row_stride][col_stride:col_stride + M])  
                # 열의 계산은 M만큼 계산하므로 현재 열의 step + M,  col_stride는 현재 열 계산의 시작 위치를 뜻함
                # 행의 이동 역시 M번 이동, row_stride는 현재 행 계산의 시작 위치를 뜻함
            if kill > best_kill:  # 가장 많은 파리수로 갱신
                best_kill = kill
    print(f'#{i} {best_kill}')