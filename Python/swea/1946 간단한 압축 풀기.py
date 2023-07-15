T = int(input())

for i in range(1, T+1):
    n = int(input())
    data = ''
    for j in range(n):
        key, val = input().split()
        data += key*int(val)  # 입력받은 알파벳들을 그 개수만큼 만든 뒤, 하나로 합로 일렬의 문자열을 생성

    print(f'#{i}')
    for k in range(0, len(data), 10):  # 일렬의 문자열을 10개 단위로 잘라냄
        print(data[k:k+10])  # end의 경우 범위를 초과해도 상관없음