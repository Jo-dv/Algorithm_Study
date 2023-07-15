from itertools import combinations
T = int(input())

for i in range(1, T+1):
    num = list(map(int, input().split()))
    res = list(set(sorted([sum(i) for i in list(combinations(num, 3))])))
    # 생성되는 조합들을 합으로하는 리스트 생성 및 정렬, 집합을 통한 중복 제거
    print(f'#{i} {res[-5]}')