keyinput, board = ["left", "right", "up", "right", "right"], [11, 11]

def solution(keyinput, board):
    x, y = 0, 0
    width, height = (board[0]-1)//2, (board[1]-1)//2  # 경계값

    for i in keyinput:
        x += -1 if i == 'left' else 1 if i == 'right' else 0
        y += -1 if i == 'down' else 1 if i == 'up' else 0
        x, y = max(min(0+x, width), -width), max(min(0+y, height), -height)  # 실시간 갱신에 따른 경계값 보정
    return [x, y]

print(solution(keyinput, board))