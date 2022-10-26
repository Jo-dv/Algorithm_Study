for i in range(1, 11):
    N, password = input().split()
    password = list(password)

    while True:
        idx = 0  # pair의 위치 기록, index를 사용하여 위치를 기록한다면 값이 중복되어 있을 경우 앞의 idx를 반환하므로 오차가 발생
        for j, k in zip(password[:-1], password[1:]):  # 한 pair씩 비교
            if j == k:  # pair가 동일하다면
                password.pop(idx)  # pair의 첫 idx를 제거한다.
                password.pop(idx)  # 첫 idx를 제거하면 나머지 pair는 왼쪽으로 밀리므로 나머지 pair의 idx는 첫 idx가 된다. 
                break  # 다음 pair를 탐색하기 위해 break
            idx += 1  # idx 오차를 방지하기 위해 반복에 따라 idx를 갱신
        else:  # 문자열에 더 이상 pair가 존재하지 않는다면
            break
    print(f'#{i}', ''.join(password))