for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    set_1 = set(input().split())
    set_2 = set(input().split())
    answer = len(set_1 & set_2)  # 교집합의 길이
    print(f'#{t} {answer}')