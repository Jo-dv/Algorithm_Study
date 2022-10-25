from collections import Counter
T = int(input())

for i in range(1, T+1):
    a, b, c = map(int, input().split())
    temp = Counter([a, b, c])  # 빈도를 세기 위해 Counter 사용
    print(f'#{i} {temp.most_common()[-1][0]}')  # 빈도가 가장 적은 것이 구하고자 하는 변수의 길이(key), value는 빈도에 해당