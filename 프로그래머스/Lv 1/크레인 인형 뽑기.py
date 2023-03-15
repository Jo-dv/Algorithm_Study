board = [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 3],
         [0, 2, 5, 0, 1],
         [4, 2, 4, 4, 2],
         [3, 5, 1, 3, 1]]
        # 1  2  3  4  5
moves = [1, 5, 3, 5, 1, 2, 1, 4] # 이동 위치


def solution(board, moves):
    answer = 0
    store = []

    for i in moves:
        for j in range(len(board)):
            item = board[j][i - 1]
            if item != 0:
                store.append(item)
                board[j][i - 1] = 0
                if len(store) >= 2 and store[-1] == store[-2]:
                    store.pop()
                    store.pop()
                    answer += 2
                break
    return answer

print(solution(board, moves))