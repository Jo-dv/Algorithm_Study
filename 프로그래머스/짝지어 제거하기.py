s = 'baabaa'

def solution(s):
    s = [i for i in s]
    temp = []

    while s:
        temp.append(s.pop())
        if len(temp) > 1 and temp[-1] == temp[-2]:
            temp.pop()
            temp.pop()

    if not temp:
        return 1
    else:
        return 0

print(solution(s))

