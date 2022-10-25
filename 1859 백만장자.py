T = int(input())  # 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

for i in range(1, T + 1):
    N = int(input())  # 각 테스트 케이스 별로 첫 줄에는 자연수 N(2 ≤ N ≤ 1,000,000)이 주어지고, 코드 상에선 더미 코드
    price = list(map(int, input().split()))  # 각 날의 매매가를 나타내는 N개의 자연수들이 공백으로 구분되어 순서대로 주어진다.
    profit = 0
    max_profit = price[-1]

    for j in range(len(price)-1, -1, -1):  # 뒤에서부터 순회
        if price[j] >= max_profit:  # 기존 최대보다 큰 값을 발견했을 경우
            max_profit = price[j]  # 해당 값으로 최대값 갱신
            continue
        profit += (max_profit - price[j])  # 최대값의 변경이 없을 경우 최대 가격에서 현재 가격을 뺌
    print(f'#{i} {profit}')

    # 앞에서부터 순회할 경우 max를 사용한 접근법은 동일한 max가 존재할 때 위치(가장 뒤)도 고려해야 하기 때문에 구현하기 복잡함