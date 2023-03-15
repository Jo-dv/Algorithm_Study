my_string = 'cccCCC'

def solution(my_string):
    return ''.join([i.upper() if i.islower() else i.lower() for i in my_string])

print(solution(my_string))