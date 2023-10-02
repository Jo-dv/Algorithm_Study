T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())

    print(f'#{i} {A * B if 1<= A <= 9 and 1 <= B <= 9 else -1}')