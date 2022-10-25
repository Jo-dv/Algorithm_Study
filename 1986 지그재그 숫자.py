T = int(input())

for i in range(1, T+1):
    N = int(input())

    res = sum([-i if i % 2 == 0 else i for i in range(1, N+1)])  # 짝수는 음수, 홀수는 양수로 초기화한 후 합
    print(f'#{i} {res}')