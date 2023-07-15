for i in range(1, int(input())+1):
    n, m = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w.sort(reverse=True)  # 큰 순으로 정렬
    t.sort(reverse=True)
    answer = 0

    for j in range(m):  # 트럭을 하나씩
        for k in range(n):  # 컨테이너와 비교
            if 0 < w[k] <= t[j]:  # 컨테이너가 트럭에 실을 수 있는 최대 무게이면서 허용 무게면
                answer += w[k]  # 전체 무게 갱신
                w[k] = t[j] = 0  # 화물에 실었으므로 0으로 처리
                break  # 반복 탈출

    print(f'#{i} {answer}')