my_string = 'We are the world'

def solution(my_string):
    dic = {i: 0 for i in my_string}
    return ''.join(dic.keys())

print(solution(my_string))