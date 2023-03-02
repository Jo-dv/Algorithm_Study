lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

def solution(lottos, win_nums):
    answer = [6] * 2
    rank = {key: value for key, value in zip(range(6, 1, -1), range(1, 6))}
    unknown = lottos.count(0)
    match = 0
    for i in lottos:
        if i in win_nums:
            match += 1

    if unknown == 6:
        return [1, 6]
    if match in rank.keys():
        answer[1] = rank[match]
    if match+unknown in rank.keys():
        answer[0] = rank[match+unknown]

    return answer

print(solution(lottos, win_nums))