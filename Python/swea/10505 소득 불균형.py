T = int(input())

for i in range(1, T+1):
    N = int(input())
    income = list(map(int, input().split()))
    average = sum(income) // len(income)
    res = [i for i in income if i <= average]

    print(f'#{i} {len(res)}')
