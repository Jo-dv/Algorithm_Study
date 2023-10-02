polynomial = '3x + 7 + x'

# 문제 설명이 착각하기 쉬움, 다항식은 다항식 및 숫자 혹은 다항식 혹은 숫자, 이 세 가지의 유형을 가짐

def solution(polynomial):
    x_num = [i for i in polynomial.split() if i != '+' and not i.isdigit()]  # x를 추출
    x_num = sum([int(i[:-1]) if len(i) > 1 else 1 for i in x_num])  
    # 추출한 x에서 계수를 추출, 길이가 1이상이면 2이상의 계수를 가진다는 의미이므로 x를 제외한 문자를 추출하여 정수로 변환하여 합산
    x = 'x' if x_num == 1 else '' if x_num == 0 else str(x_num)+'x'
    # 합산 값이 1이라면 계수는 1이라서 생략, 계수가 없다면 x가 없다는 의미, 그렇지 않으면 계수와 x를 붙여서 일차항 계산
    num = sum([int(i) for i in polynomial.split() if i.isdigit()])
    # 주어진 문제에서 상수항만을 추출하여 합산
    return x + (' + ' + str(num) if x != '' and num != 0 else '' if num == 0 else str(num))
    # 일차항이 존재하며 상수항이 0이 아니라면 + 상수항의 형태로 출력, 그렇지않고 상수만 없다면 상수 생략, 마지막으로 일차항이 없다면 상수항만 출력

print(solution(polynomial))