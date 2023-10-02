from heapq import *

for t in range(1, int(input())+1):
    n = int(input())
    op = [input() for _ in range(n)]
    tree = []
    answer = []

    for i in op:
        if i[0] == '1':  # 삽입 연산인 경우
            data = int(i.split()[1])  # 데이터만 따로 추출
            heappush(tree, (-data, data))  # 최대 힙
        else:
            if not tree:  # 트리 상태 확인 후, 빈 트리인데 데이터를 제거할 경우
                answer.append(-1)  # -1 저장
            else:
                answer.append(heappop(tree)[1])  # 키로 사용하는 음수값이 아닌 원 데이터만 저장

    print(f'#{t}', *answer)