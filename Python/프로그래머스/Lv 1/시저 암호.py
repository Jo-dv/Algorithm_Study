s = 'a B z'
n = 4

def solution(s, n):
    answer = ''
    for i in s:
        target = ord(i) + n
        if ord('z') < target:
            answer += chr(ord('a') + (target - ord('z') - 1))
        elif ord(i) < ord('Z') < target:
            answer += chr(ord('A') + (target - ord('Z') - 1))
        elif i == ' ':
            answer += i
        else:
            answer += chr(ord(i) + n)
    return answer

print(solution(s, n))