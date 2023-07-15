for t in range(1, int(input())+1):
    n = int(input())
    answer1, answer2, answer3 = (n * (n + 1))//2, n**2, n * (n + 1)
    # 처음엔 단순 조건부 반복을 통해 계산 -> 제한시간 초과
    # n을 바탕으로 3, 5, 6에 대해 각각의 제약 사항에 대한 값으로 패턴 도출
    # 첫 제약 사항에 대해선 (n / 2) * (n + 1)로 도출했으나, 답 틀림. 다시 보니 세 번째 제약 조건식에 절반임을 알아챔
    print(f'#{t} {answer1} {answer2} {answer3}')