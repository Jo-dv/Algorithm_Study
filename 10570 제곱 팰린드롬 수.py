T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())
    count = 0

    for N in range(A, B+1):
        if str(N) == str(N)[::-1] and str(int(N**0.5)) == str(int(N**0.5))[::-1] and N % (N**0.5) == 0.0:
            # N에 대한 팰린드롬 and 루트 N에 대한 팰린드롬, 단 소수점을 날리기 위해 정수로 변환, 이 때 소수도 정수가 되어버리기 떼문에
            # N을 루트 N을 나눴을 때 나머지가 0.0(정수에서 소수로 나눠서 떨어진다면 그 값은 0이 아닌 0.0)이라면 팰린드롬
            # ex N = 9, 루트 N = 3.0이면 나머지는 0.0이므로 팰린드롬 성립
            count += 1
    print(f'#{i} {count}')