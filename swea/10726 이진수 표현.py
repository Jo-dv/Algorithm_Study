for t in range(1, int(input())+1):
    N, M = map(int, input().split())

    if bin(M)[2:][-N:] == '1'*N:  # 이진수 부분([2:])의 마지막 N비트: 뒤에서 N번째 자리부터 끝까지 모두 11..1이라면
        print(f'#{t} ON')
    else:
        print(f'#{t} OFF')
