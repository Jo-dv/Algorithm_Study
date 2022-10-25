T = int(input())  # 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고

for i in range(1, T+1):
    test_case = list(map(int, input().split()))  # 그 아래로 각 테스트 케이스가 주어진다.
    modified_case = [i for i in test_case if i % 2 != 0]  # 입력받은 테스트 케이스에서 홀수만 추림
    res = 0
    for j in modified_case:
        res += j
    print(f'#{i} {res}')