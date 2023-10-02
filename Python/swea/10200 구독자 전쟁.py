for i in range(1, int(input())+1):
    N, A, B = map(int, input().split())

    P = set(range(1, A + 1)) if A > 0 else set()  # 0이면 공집합, 아니라면 해당 인원들로 채워진 집합 생성, 숫자는 의미 없음
    T = set(range(1, B + 1)) if B > 0 else set()
    maximum = len(P & T)  # 교집합의 길이는 모두 P와 T를 구독하는 구독자의 수의 최대
    minimum = A + B - N if A + B > N else 0  # 양쪽 구독자 수의 합이 전체 인원보다 클 경우, 남은 인원이 최소 아니라면 최소 인원은 0
    print(f'#{i} {maximum} {minimum}')
