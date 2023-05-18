t = int(input())
test_case = []

for _ in range(t):  # 테스트 케이스가 많은 관계로 따로 나눠서 저장
    test_case.append(map(int, input().split()))

for t in range(1, t+1):
    a, b, c, d = test_case[t-1]  # 테스트 케이스를 하나씩 불러와서
    end = max(a, b, c, d)  # 상한값 저장
    arr = [1 if a < i <= b else 0 for i in range(end + 1)]  # 상한값을 인덱스로 가지는 리스트 생성, 전구 X 초기화
    for i in range(c + 1, d + 1):  # 전구 Y의 시간
        arr[i] += 1
    print(f'#{t} {arr.count(2)}')  # 값이 2인 부분은 두 전구가 동시에 켜져있는 부분

'''
t = int(input())
test_case = []

for _ in range(t):
    test_case.append(map(int, input().split()))

for t in range(1, t+1):  # 도식화 풀이
    a, b, c, d = test_case[t-1]
    exp = min(b, d) - max(a, c)  # 그림을 그려보면 쉽게 파악 가능
    print(f'#{t} {0 if exp <= 0 else exp}')  # 0이하면 겹치는 부분이 없다는 뜻
'''