my_string, num1, num2 = 'hello', 1, 2

def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1], s[num2] = s[num2], s[num1]
    return ''.join(s)

print(solution(my_string, num1, num2))