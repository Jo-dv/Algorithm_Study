my_string = 'bus'

def solution(my_string):
    answer = ''

    for i in my_string:
        answer += '' if i in ['a', 'e', 'i', 'o', 'u'] else i

    return answer

print(solution(my_string))