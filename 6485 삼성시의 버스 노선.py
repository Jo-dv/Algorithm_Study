for t in range(1, int(input())+1):
    N = int(input())
    lines = [list(map(int, input().split())) for _ in range(N)]
    P = [[int(input()), 0] for N in range(int(input()))]  # 유사 hash의 형태, hash로 풀면 중복 key, 같은 key에 대해 value 누적합 

    for line in lines:
        for i in P:  # 문제 그대로 해석할 것, 입력 받은 P에 대해 모두 확인, P가 [1, 1, 1, 1]이라면 이 네 개에 대해 계산
            if line[0] <= i[0] <= line[1]:  # 입력 받은 정류장의 번호가 범위 안이라면
                i[1] += 1  # 갱신

    res = [i[1] for i in P]  # 노선의 수만 추려냄

    print(f'#{t}', *res)