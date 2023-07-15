T = int(input())

for i in range(1, T+1):
    N = int(input())
    component = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}  # 요소와 요소의 개수
    cur = 0

    while N != 1:  # 다 나눌 때 까지
        target = list(component.keys())[cur]  # cur가 가리키는 요소
        if N % target == 0:  # 해당 요소로 나누어 떨어진다면
            N //= target  # N을 해당 수로 나눔
            component[target] += 1  # 해당 요소의 개수를 증가
        else:
            cur += 1  # 더 이상 cur가 가리키는 요소로 나누어 떨어지지 않는다면 다음 요소를 가리킴

    print(f'#{i}', *list(component.values()))