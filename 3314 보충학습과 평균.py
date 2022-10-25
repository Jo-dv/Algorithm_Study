T = int(input())

for i in range(1, T+1):
    score = list(map(int, input().split()))
    res = [i if i > 40 else 40 for i in score]
    print(f'#{i}', sum(res) // len(res))