s = "Zbcdefg"

def solution(s):
    answer = ''
    temp = [ord(i) for i in s]
    temp.sort(reverse=True)
    temp = [chr(i) for i in temp]
    for i in temp:
        answer += i
    return answer

print(solution(s))