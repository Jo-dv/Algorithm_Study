n = int(input())
a = list(map(int, input().split()))

rank = {}  # 순위를 저장할 딕셔너리
for i, x in enumerate(sorted(set(a))):  # 중복을 제거하고 정렬하여
    rank[x] = i  # 그 값을 키로하여 순서를 저장

print(*[rank[x] for x in a])  # 원본 값을 키로하여 값 추출
