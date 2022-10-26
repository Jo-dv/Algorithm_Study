for i in range(1, 11):
    case = int(input())
    puzzle = [input() for _ in range(100)]  # 가로 검사
    t_puzzle = [''.join(i) for i in zip(*puzzle)]  # 세로 검사
    best = 0

    for j, k in zip(puzzle, t_puzzle):
        for n in range(1, 101):  # 찾고자 하는 회문의 길이, 최소 1 ~ 최대 100
            for l in range(100-n+1):
                if j[l:l+n] == j[l:l+n][::-1]:
                    best = max(best, len(j[l:l+n]))
                if k[l:l+n] == k[l:l+n][::-1]:
                    best = max(best, len(k[l:l+n]))
    print(f'#{i} {best}')