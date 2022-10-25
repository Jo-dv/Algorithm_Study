T = int(input())  # 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

n = [str(i) for i in range(1, T+1)]  # T개의 문자열 숫자로 이루어진 리스트 생성

for i in n:
    if '3' in i or '6' in i or '9' in i:  # 문자열을 하나씩 꺼내서 구성 숫자 확인
        t = i.count('3') + i.count('6') + i.count('9')  # 조건에 부합한다면 숫자 카운팅
        print('-'*t, end='')  # 등장하는 숫자만큼 출력
        print(end=' ')  # 출력후 한 칸 띄어줌
    else:
        print(i, end=' ')