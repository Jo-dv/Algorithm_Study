priorities = [1, 1, 9, 1, 1, 1]
location = 0

def solution(priorities, location):
    answer = []

    for i in range(len(priorities)):
        answer.append((priorities[i], chr(65 + i)))

    target = answer[location]

    i = 0
    while True:
        first = max(answer, key=lambda x: (x[0], -ord(x[1])))
        if first[0] > answer[0][0]:
            answer.append(answer.pop(0))
        else:
            i += 1
            if answer.pop(0) == target:
                break

    return i

print(solution(priorities, location))