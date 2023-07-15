answers = [3, 3, 1, 1, 2, 2, 4, 4]

def solution(answers):
    answer = []
    marker = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    best = 0
    for i in range(len(marker)):
        pos = rank = 0
        for j in range(len(answers)):
            if pos == len(marker[i]):
                pos = 0
            if marker[i][pos] == answers[j]:
                rank += 1
            pos += 1

        if best <= rank:
            if answer and best != rank:
                answer.pop()
            best = rank
            answer.append((i + 1, rank)[0])
    return answer

print(solution(answers))