my_string = 'aAb1B2cC34oOp'

def solution(my_string):
    answer, check = [], ''
    for i in my_string:
        if i.isdigit():  # 탐색에서 숫자를 만날 경우 추가, 이 경우 true일 때는 다음 탐색으로 넘어감
            check += i
        else:
            if check:  # 문자를 만났을 때 check에 값이 저장되어 있다면
                answer.append(int(check))  # 해당 값을 추가하고
                check = ''  # 초기화
    return sum(answer) + (int(check) if check else 0)  # 숫자가 마지막에 있어서 저장되지 못했을 경우 이를 확인하고 계산

'''
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)  # 숫자가 연속적이라면 공백없이 붙어있을 것이고 아니라면 공백이 있을 것
    return sum(int(i) for i in s.split())
'''

print(solution(my_string))