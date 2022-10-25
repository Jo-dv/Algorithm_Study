for i in range(1, 11):
    n = int(input())
    puzzle = [input() for _ in range(8)]  # 가로 검사
    t_puzzle = [''.join(i) for i in zip(*puzzle)]  # 세로 검사
    count = 0

    for j, k in zip(puzzle, t_puzzle):  # 각각에서 한 줄씩 가져와
        for l in range(8-n+1):
            # 왼쪽부터 한 칸씩 이동해서 n의 길이를 가진 문자열을 검사
            # 길이는 항상 8이고 찾고자 하는 문자열의 길이가 n이라면 한 칸씩 8-n+1 번만 이동하면 문자열의 끝이 puzzle의 끝이 됨
            if j[l:l+n] == j[l:l+n][::-1]:  # 가로의 해당 문자열과 그 문자열의 역순이 같다면
                count += 1
            if k[l:l+n] == k[l:l+n][::-1]:  # 세로의 해당 문자열과 그 문자열의 역순이 같다면
                count += 1
    print(f'#{i} {count}')