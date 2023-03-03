my_strings = 'aAb1B2cC34oOp'

def solution(my_string):
    return sum([int(i) for i in my_string if i.isdigit()])

print(solution(my_strings))