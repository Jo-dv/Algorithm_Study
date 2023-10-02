from sys import stdin

n, m = map(int, input().split())
dic = {}

for _ in range(n):
    site, pw = stdin.readline().rstrip().split()
    dic[site] = pw

for _ in range(m):
    print(dic[stdin.readline().rstrip()])

# 단순 딕셔너리 저장 및 탐색, 딕셔너리 아는지 모르는지 확인하는 문제