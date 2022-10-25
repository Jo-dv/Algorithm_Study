from collections import deque

def process(data, pre):  # 이를 방지하고자 별도의 함수 정의
    if data[-1] != 0:  # 함수의 수행도 종료 조건이 아닐 때만 수행, 단 호출은 계속
        return data.append(max(data.popleft() - pre, 0))  # 음수가 발생하지 않도록 limit 설정

while True:  # 이전 문제와는 다르게 매번 test case를 입력으로 받음
    try:  # test case가 있으면
        T = int(input())
        data = deque(list(map(int, input().split())))  # 문제에서 제시하는 조건 = deque
        p = 1  # process number

        while data[-1] != 0:  # 종료 조건
            if p > 5:  # 한 process가 끝나면
                p = 1  # 다시 갱신
            process(data, p)  # process 과정을 while문 내에서 한 번에 처리할 경우 중간에 조건을 만족해도 남은 process까지 계속 진행
            p += 1  # 다음 process로 갱신
        print(f'#{T}', *list(data))
    except EOFError:  # 모든 test case를 수행했을 경우
        break  # 코드 종료