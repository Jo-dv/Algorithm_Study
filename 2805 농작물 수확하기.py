T = int(input())

for i in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    res = 0
    start, end = N//2, N//2+1  # 모든 영역은 가운데 한 칸에서 시작된다.

    for j in range(N//2):  # 중간 라인 전까지
        res += (sum(farm[j][start:end]) + sum(farm[N-1-j][start:end]))  # 중간 라인을 제외하고 하나의 짝을 이루므로
        start -= 1  # 반복이 될수록 시작 지점은 한 칸씩 밀려남
        end += 1  # 반복이 될수록 종료 지점은 한 칸씩 늘어남
    res += sum(farm[N//2])  # 가운데를 제외한 모든 영역에 합산이 끝나면 가운데 영역 합산

    print(f'#{i} {res}')