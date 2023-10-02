def notation(n, x):
    res = ''
    info = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}

    while x > 0:  # 진법 변환, 조건에 맞는 수는 주어진 알파벳으로 치환
        res += info[str(x % n)] if str(x % n) in info.keys() else str(x % n)
        x //= n

    return res[::-1] if res != '' else '0'  # 0일 경우 공백이므로 0 반환

def solution(n, t, m, p):
    answer = ''
    temp = ''

    for i in range(m * t):  # 간단하게 생각해서 모든 사람이 필요한 자릿수만큼 반복
        temp += notation(n, i)

    for i in range(p-1, len(temp), m):  # 자신의 순서부터
        answer += temp[i]
        if len(answer) == t:  # 말해야 하는 길이를 달성했다면
            return answer

n, t, m, p = 16, 16, 2, 2

print(solution(n, t, m, p))