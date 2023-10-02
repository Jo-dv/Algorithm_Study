#dirs = "LLLLRLRLRLL"
#dirs = "ULURRDLLU"
dirs = 'LULLLLLLU'

def solution(dirs):
    answer = []
    position = [0, 0]
    for i in dirs:
        current_position = position.copy()
        if i == 'L' and -5 < position[0]:
            position[0] -= 1
        elif i == 'R' and position[0] < 5:
            position[0] += 1
        elif i == 'U' and position[1] < 5:
            position[1] += 1
        elif i == 'D' and -5 < position[1]:
            position[1] -= 1
        if [current_position, position.copy()] not in answer and current_position != position:
            if list(reversed([current_position, position.copy()])) not in answer:
                answer.append([current_position, position.copy()])

    return len(answer)

print(solution(dirs))