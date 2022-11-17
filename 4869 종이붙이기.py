for t in range(1, int(input())+1):
    N = int(input())
    paper = [0]*(N//10+1)

    for i in range(1, N//10+1):
        c = 2 if i % 2 == 0 else 1  # index가 짝수일 경우 2 아니라면 1이 가산됨
        paper[i] = sum(paper[:i]) + c  # 현재 index의 값은 직전까지의 값들의 총합 + index에 따른 c

    print(f'#{t} {paper[-1]}')