s = "1 2 3 4"

def solution(s):
    answer = ''
    answer += str(min(list(map(int, s.split()))))
    answer += ' ' + str(max(list(map(int, s.split()))))
    return answer

print(solution(s))