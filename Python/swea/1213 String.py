while True:  # 이전 문제와는 다르게 매번 test case를 입력으로 받음
    try:  # test case가 있으면
        T = int(input())
        target = input()
        problem = input()
        print(f'#{T} {problem.count(target)}')  # 문자열 내 target counting
    except EOFError:  # 모든 test case를 수행했을 경우
        break  # 코드 종료