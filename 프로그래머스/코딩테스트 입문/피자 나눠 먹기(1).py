n = 15

def solution(n):
    answer = divmod(n, 7)
    rest = 1 if 1 <= answer[1] <= 7 else 0  # 7의 배수명한테 피자를 다 배분하고 나머지에 대해서 나머지 인원이 있다면 한 판 더 추가
    return answer[0] + rest  # 배수명에 대한 피자 + 나머지 인원에 대한 피자

print(solution(n))
