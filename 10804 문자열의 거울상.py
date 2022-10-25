T = int(input())

mirror = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}

for i in range(1, T+1):
    problem = list(input())[::-1]  # 거울의 특성상 사물이 반대로 뒤집히므로 순서를 거꾸로 바꿔줌
    res = ''

    for j in problem:
        res += mirror[j]

    print(f'#{i} {res}')