T = int(input())
answer = 'abcdefghijklmnopqrstuvwxyz'

for i in range(1, T + 1):
    problem = input()
    count = 0

    for j, k in zip(problem, answer):
        if problem[0] != 'a' or j != k:  # 처음부터 틀렸거나 혹은 어긋나는 부분이 나타나면 탐색 종료
            break  # 문제의 조건은 일치하는 개수가 아니라 일치하는 순서 및 개수이다. 즉 틀린 것이 나온 시점부터 탐색할 필요가 없다.
        else:
            count += (j == k)  # True 값은 1이므로

    print(f'#{i} {count}')