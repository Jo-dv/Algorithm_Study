s = '(()('

def solution(s):
    answer = False
    s = list(s)
    temp = []
    while s:
        if s[-1] == ')':
            temp.append(s.pop())
        elif temp and s[-1] == '(':
            temp.pop()
            s.pop()
        else:
            break
    if not temp and not s:
        return True

    return answer

print(solution(s))