expression = input()+' '  # 종료 표시용으로 임의의 값 삽입
answer = []
num = ''
flag = 1

for i in expression:  # 값들을 하나씩 가져와서
    if i.isdigit():  # 부호가 나올 때까지 저장
        num += i
        continue
    answer.append(flag * int(num))  # 만들어진 숫자는 플래그를 곱해서 저장
    num = ''  # 다음 숫자 생성을 위해 초기화
    if i == '-' and flag == 1:  # 음수가 나왔다면 그 이후에 나오는 + 연산을 - 연산으로 바꾸기 위해
        flag = -1  # 부호 변경

print(sum(answer))  # 음수에 무조건 괄호 치면 최솟값 생성 가능, 즉 - 다음에 나오는 +를 다 -로 바꾸면 괄호를 치는 것과 동일