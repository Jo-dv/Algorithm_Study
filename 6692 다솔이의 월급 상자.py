for t in range(1, int(input())+1):
    N = int(input())
    salary = [input().split() for _ in range(N)]  # 봉급 정보를 입력 받음
    res = 0  # 봉급의 평균을 초기화

    for i in salary:
        res += float(i[0]) * int(i[1])  # 확률에 대한 평균, 즉 기댓값: E(X) = sum(pi * xi) | i = 1 ... n
    print(f'#{t} {res}')