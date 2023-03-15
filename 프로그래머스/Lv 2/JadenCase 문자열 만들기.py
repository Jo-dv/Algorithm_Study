s = '3people unFollowed me'

def solution(s):
    answer = ''

    for index, i in enumerate(s):
        if answer and answer[-1] == ' ' and i != ' ' or index == 0 and i.isalpha():
            answer += i.upper()
        else:
            answer += i.lower()
    return answer

print(solution(s))