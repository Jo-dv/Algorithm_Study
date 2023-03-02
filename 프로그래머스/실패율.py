N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

def solution(N, stages):
    temp = []

    for i in range(1, N + 1):
        if i not in stages:
            ratio = 0
        else:
            ratio = stages.count(i) / len([x for x in stages if x >= i])
        temp.append([i, ratio])
        temp.sort(key=lambda x: (-x[1], x[0]))

    answer = [[i][0] for i, [i][0] in temp]
    return answer

print(solution(N, stages))