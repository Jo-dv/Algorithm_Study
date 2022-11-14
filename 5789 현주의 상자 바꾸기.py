for t in range(1, int(input())+1):
    N, Q = map(int, input().split())
    boxes = [0] * N  # N 길이의 0으로 구성된 초기 list 생성

    for i in range(1, Q+1):  # 삽입하는 번호는 시행 횟수 i와 같다.
        L, R = map(int, input().split())  # 범위를 입력
        for j in range(L-1, R):  # index는 0부터 시작하므로 실제 범위에 -1, for문의 특성상 끝 범위는 자연스럽게 -1
            boxes[j] = i

    print(f'#{t}', *boxes)  # unpacking