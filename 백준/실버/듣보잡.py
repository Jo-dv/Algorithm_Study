from sys import stdin

n, m = map(int, input().split())

no_see, no_listen = set(stdin.readline().rstrip() for _ in range(n)), set(stdin.readline().rstrip() for _ in range(m))
answer = no_see & no_listen  # 단순 집합 생성하여 교집합 구하기, 일반적인 입력으로 초기화하면 매우 느림

print(len(answer))
for i in sorted(answer):
    print(i)