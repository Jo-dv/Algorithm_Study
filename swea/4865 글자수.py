for t in range(1, int(input())+1):
    str1 = input()
    str2 = input()
    board = {i: 0 for i in str1}  # str1 글자들을 key로 하는 dictionary 생성

    for i in str2:
        if i in board.keys():  # str2의 글자가 str1에 포함되어 있다면
            board[i] += 1

    print(f'#{t} {max(board.values())}')