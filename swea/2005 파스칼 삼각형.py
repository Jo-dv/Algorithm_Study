T = int(input())

for i in range(1, T+1):
    N = int(input())
    tri = [[1 if j == 0 or i == j else 0 for j in range(N)] for i in range(N)]  # N x N 매트릭스 생성
    # 문제 조건에 맞춰 꼭지점과 변에 해당하는 부분을 먼저 1로 채움, 첫 열과 대각선이 변에 해당

    if N >= 3:  # 매트릭스를 생성할 때 N <= 2까지 커버가능
        for j in range(2, N):  # 행은 index 상 2부터 시작
            for k in range(1, N):  # 열은 index 상 1부터 시작
                tri[j][k] = tri[j-1][k-1] + tri[j-1][k]  # 오른쪽 위와 바로 위의 값

    print(f'#{i}')
    for j in tri:
        for k in j:
            if k != 0:  # 매트릭스의 0을 출력하지 않고 문제 출력 형식에 맞추기 위함
                print(k, end=' ')
            else:  # 0부터는 더 이상 출력 및 조건을 검사할 필요가 없으므로 넘어감
                continue
        print()  # 행의 출력이 완료될 때마다 개행