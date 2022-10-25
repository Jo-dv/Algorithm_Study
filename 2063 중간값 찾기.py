N = int(input())  # 입력은 첫 줄에 N 이 주어진다.

score = sorted(list(map(int, input().split())))  # 둘째 줄에 N 개의 점수가 주어진다. 중간값을 찾기 위해 정렬
print(score[N // 2])  # N은 항상 홀수이므로 N을 2로 //을 통해 나누면 항상 중간값에 해당하는 index가 됨