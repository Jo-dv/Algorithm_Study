from string import ascii_lowercase

age = 23

def solution(age):
    answer = {str(i): j for i, j in zip(range(10), ascii_lowercase[:10])}
    return ''.join([answer[i] for i in str(age)])

print(solution(age))