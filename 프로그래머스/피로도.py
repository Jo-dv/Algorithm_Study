k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]


def solution(k, dungeons):
    global answer
    answer = 0
    least = [i[0] for i in dungeons]
    consume = [i[1] for i in dungeons]
    visit = [False] * len(dungeons)

    def problem(k, comp=0):
        global answer
        answer = max(answer, comp)

        for i in range(len(dungeons)):
            if not visit[i] and k >= least[i]:
                visit[i] = True
                problem(k - consume[i], comp + 1)
                visit[i] = False

    problem(k)
    return answer

print(solution(k, dungeons))