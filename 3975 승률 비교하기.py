res = []  # 결과 저장 list
ra = res.append  # 반복문에서 apeend를 수행하지 않고 밖같에서 정의하여 parameter만 넘겨주면 훨씬 빠르다,

for t in range(1, int(input())+1):
    aw, an, bw, bn = map(int, input().split())
    a, b = aw / an, bw / bn

    if a > b:
        ra(f'#{t} ALICE')
    elif a < b:
        ra(f'#{t} BOB')
    else:
        ra(f'#{t} DRAW')

for i in res:  # 저장된 값들을 새로운 반복을 통해 재출력
    print(i)