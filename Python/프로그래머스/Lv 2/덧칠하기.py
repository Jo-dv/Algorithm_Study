n, m, section = 8, 4, [2, 3, 6]

def solution(n, m, section):
    answer = 0
    x = [0]*len(range(n+1))  # 전체 벽 생성
    for i in section:  # 칠해야 하는 구간
        if not x[i]:  # 해당 구간이 칠해져 있지 않다면
            x[i:i + m] = [1] * len(x[i:i + m])
            # 해당 벽부터 m미터까지 칠함, len을 해주지 않으면 인덱스가 끝에 위치할 경우 불필요하게 리스트가 길어짐
            answer += 1
    return answer

print(solution(n, m, section))