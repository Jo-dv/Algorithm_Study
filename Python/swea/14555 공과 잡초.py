for t in range(1, int(input()) + 1):
    case = list(input())
    ball = 0

    for i in range(len(case) - 1):  # pair만 검사하므로 list의 길이 -1 까지만 검사
        if (case[i] == '(' and case[i + 1] == ')') or (case[i] == '(' and case[i + 1] == '|'):
            ball += 1
        elif case[i] == '|' and case[i + 1] == ')':
            ball += 1

    print(f'#{t} {ball}')
    # 문제가 애매, 공은 (), (|, |)로 표현된다. 이것들의 수를 count
    # 놓았을 수의 뜻은 이미 놓인 공을 포함, 공이 놓여있을 수 있던 곳도 count하는 것이 관건
    # (|나 |)는 공은 아니지만 괄호로 인해 공이 있었다는 것을 알 수 있음
