s = "one4seveneight"

def solution(s):
    char = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    strings = ''
    answer = ''
    for i in s:
        if not i.isdecimal():
            strings += i
            if strings in char:
                answer += str(char.index(strings))
                strings = ''
        else:
            answer += i
    return int(answer)

print(solution(s))