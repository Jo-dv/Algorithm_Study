T = int(input())  # 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고

for i in range(1, T+1):
    test_case = list(map(int, input().split()))  # 그 아래로 각 테스트 케이스가 주어진다.
    print(f'#{i} {round(sum(test_case) / len(test_case))}')