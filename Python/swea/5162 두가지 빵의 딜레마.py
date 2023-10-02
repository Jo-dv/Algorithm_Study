for t in range(1, int(input())+1):
    A, B, C = map(int, input().split())
    res = C // min(A, B)  # 가격이 제일 저렴한 걸 많이 사면되므로 현재 금액에서 저렴한 빵의 가격을 나눠 몫을 구한다.
    print(f'#{t} {res}')