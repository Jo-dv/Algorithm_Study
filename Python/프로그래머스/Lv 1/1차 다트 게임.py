import re

dartResult = '1S2D*3T'

def solution(dartResult):
    answer = [0] * 3
    score = re.findall('[0-9][0-9]*', dartResult)
    score = [int(i) for i in score]
    bonus = re.findall('[A-Z]', dartResult)
    bonus = [1 if i == 'S' else 2 if i == 'D' else 3 for i in bonus]
    option = re.findall('[0-9][A-Z](\*|#)?', dartResult)
    # test = re.findall('[0-9][0-9]*[A-Z][*|#]?', dartResult)

    for i in range(3):
        answer[i] = score[i] ** bonus[i]
        if option[i] == '*':
            answer[i] *= 2
            answer[i - 1] *= 2
        if option[i] == '#':
            answer[i] *= -1

    return sum(answer)

print(solution(dartResult))


