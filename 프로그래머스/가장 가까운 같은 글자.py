s = 'banana'

def solution(s):
    answer, loc = [], {i: -1 for i in set(s)}  # 초기 위치는 -1로 초기화
    for i, j in enumerate(s):
        answer.append(-1) if loc[j] == -1 else answer.append(i-loc[j])  # 초기 위치가 갱신 안 되어 있다면 -1 아니면 위치의 차
        loc[j] = i  # 최근 위치 갱신

    return answer

print(solution(s))
