my_strings = 'jaron'

def solution(my_string):
    answer = ''.join(reversed(my_string))
    return answer

print(solution(my_strings))