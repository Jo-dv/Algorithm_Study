from collections import deque

my_string = '3 + 4 - 15 + 30'

def solution(my_string):
    num, op = deque([]), deque([])
    for i in my_string.split():
        num.append(int(i)) if i.isdigit() else op.append(i)  # 숫자와 연산자 분할

    n = num.appendleft
    while len(num) > 1:  # 최종 결과가 나올 때까지 분할한 숫자와 연산자를 통해 계산해서 다시 저장
        n(num.popleft() + num.popleft()) if op.popleft() == '+' else n(num.popleft() - num.popleft())

    return sum(num)

print(solution(my_string))