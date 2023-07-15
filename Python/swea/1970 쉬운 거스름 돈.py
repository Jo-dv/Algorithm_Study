T = int(input())

for i in range(1, T+1):
    balance = {50000: 0, 10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 0, 50: 0, 10: 0}  # greed search를 위한 dictionary
    change = int(input())

    for j in balance.keys():  # greed search
        if change % j != change:  # 현재 금액(j)으로 나눴을 때 값이 거스름돈과 다르다면 현재 금액으로 나눌 수 있다는 의미
            balance[j] = (change // j)  # 이 때의 몫은 필요한 금액의 양이 되며
            change %= j  # 나머지는 그 금액을 제외한 양이 됨
    print(f'#{i}')
    print(*list(balance.values()))