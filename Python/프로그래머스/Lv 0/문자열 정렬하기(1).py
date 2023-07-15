my_strings = 'hi12392'

def solution(my_string):
    return sorted([int(i) for i in my_string if i.isdigit()])

print(solution(my_strings))