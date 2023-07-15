def solution(k, ranges):
    t = k
    c, answer = [0], []
    while t != 1:
        t = t * 3 + 1 if t % 2 else t // 2  # 콜라츠 추측
        c.append(c[-1] + (min(k, t) + max(k, t)) / 2)  # 을 이용한 너비의 누적합(=정적분)
        k = t  # k는 직전의 y값이므로 다음 계산을 위해 갱신

    for a, b in ranges:
        b += len(c)-1  # 초기 0을 제외한 길이 즉 원래의 k
        answer.append(-1.0) if a > b else answer.append(c[b] - c[a])
        # a와 b가 같다면 0, b가 크다면 적분값이므로 적분식으로 표현 가능

    return answer


k, ranges = 5, [[0,0],[0,-1],[2,-3],[3,-3]]

print(solution(k, ranges))