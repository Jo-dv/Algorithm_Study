for t in range(1, int(input())+1):
    N, D = map(int, input().split())
    res = divmod(N, D*2+1)  # 한 좌표에 심었을 때 커버할 수 있는 꽃의 수 = D*2+1

    if res[1] != 0:  # 정원의 꽃들을 커버할 수 있는 꽃의 수로 나눴을 때, 나머지가 있다면
        print(f'#{t} {res[0] + 1}')  # 몫 + 1이 분무기의 수
    else:  # 나눠 떨어진다면
        print(f'#{t} {res[0]}')  # 몫이 분무기의 수
