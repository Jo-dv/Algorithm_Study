s = 'a123'

def solution(s):
    answer = False
    if len(s) == 4 or len(s) == 6:
        if s.isdecimal(): # value를 int로 변환할 수 있는지 여부
            answer = True
    return answer

print(solution(s))