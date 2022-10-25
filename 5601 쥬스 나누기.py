T = int(input())

for i in range(1, T+1):
    N = int(input())
    ans = ('1/' + str(N) + ' ') * N  # 1/N을 공백을 포함하여 N번 반복하면 된다.

    print(f'#{i}', ans.rstrip())  # 우측 공백 제거