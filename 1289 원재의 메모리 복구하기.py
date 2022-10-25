T = int(input())

for i in range(1, T + 1):
    original = input()
    init = ''.zfill(len(original))  # 원래 값의 길이만큼 0으로 채워 초기 값 생성
    count = 0

    while original != init:  # 원래 값과 초기 값이 다르다면
        temp = ''  # 처리된 값을 저장할 임시 변수
        for j, k in zip(original, init):
            if j == k:  # 한 자리씩 비교해서
                temp += k  # 같다면 별도의 처리를 수행하지 않고 넘어감
                continue
            else:
                temp += j*(len(original)-len(temp))  # 다르다면 원래의 값으로 끝까지 덮어씌운 값은 변수에 저장후 종료
                break
        init, temp = temp, ''  # 초기 값을 처리된 변수로 갱신하고 임시 변수는 다시 초기화
        count += 1  # 처리 과정이 끝났으니 처리 횟수 증가
    print(f'#{i} {count}')