from sys import stdin

n, m = map(int, input().split())
pokedex = {stdin.readline().rstrip(): i for i in range(1, n+1)}  # 이름 포켓몬 도감 생성
pokedex_no = list(pokedex.keys())  # 숫자 포켓몬 도감 생성

for _ in range(m):
    problem = stdin.readline().rstrip()
    print(pokedex_no[int(problem)-1]) if problem.isdigit() else print(pokedex[problem])