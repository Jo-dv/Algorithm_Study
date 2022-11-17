for t in range(1, int(input())+1):
    case = list(input())
    stack = []
    ans = 1

    for i in case:
        if i == '(' or i == '{':  # 여는 괄호는 추가
            stack.append(i)
        elif i == ')' or i == '}':  # 닫는 괄호라면
            if stack:  # 스택이 채워져 있다면
                check = stack.pop()  # 가장 최근 값을 가져와서
                if check == '(' and i != ')' or check == '{' and i != '}':  # 짝이 맞는지 확인
                    ans = 0  # 짝이 안 맞다면 
            else:  # 닫힌 괄호의 짝을 검사해야 하는데 검사할 스택이 비어있다면
                ans = 0  # ())의 경우가 그러함
    if stack:  # 문자열의 검사가 끝났는데 아직 스택에 값이 있다면
        ans = 0  # (()의 경우가 그러함

    print(f'#{t} {ans}')