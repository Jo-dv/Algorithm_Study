T = int(input())

for i in range(1, T+1):
    N, K = map(int, input().split())
    score = sorted([i for i in map(int, input().split())], reverse=True)

    print(f'#{i} {sum(score[:K])}')  # 내림차순으로 정렬 후, 처음부터 K까지의 점수를 합함