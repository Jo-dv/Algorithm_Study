T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    twin = N - M  # N은 최소 M(모두 uni)에서 2M(모두 twin) 사이, 주어진 뿔에서 본 동물을 빼면 twin의 수가 됨
    uni = M - twin  # 본 동물에서 twin을 빼면 나머지는 uni의 수가 됨

    print(f'#{i} {uni} {twin}')