def problem(ref, N, M):
    if N == ref**M:  # 재귀를 통해 갱신된 N이 원래 입력에 대한 N의 M 거듭제곱일 때
        return N  # 갱신된 N 반환
    return problem(ref, N*ref, M)  # 원래 입력을 살리기 위해 ref를 사용해서 N을 거듭제곱 값으로 갱신

while True:
    try:
        T = int(input())
        N, M = map(int, input().split())
        print(f'#{T} {problem(N, N, M)}')
    except EOFError:
        break