T = int(input())

for i in range(1, T+1):
    N, K = map(int, input().split())
    no_submit = set(map(int, input().split()))  # 제출하지 않은 사람
    submit = set([i for i in range(1, N+1)])  # 제출한 사람

    print(f'#{i}', *list(submit - no_submit))  # 차집합