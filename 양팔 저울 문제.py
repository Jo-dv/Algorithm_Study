import random


def solution(problems):
    def balance(coins):
        idx1 = len(coins) // 3  # 1/3
        idx2 = len(coins) // 3 * 2  # 2/3

        a, b, c = coins[0:idx1], coins[idx1:idx2], coins[idx2:]  # 동전을 세 묶음으로 나눔

        if len(coins) == 3:  # 3개의 동전만 남았다면
            if coins[0] > coins[-1]:  # a와 c를 비교해서 a가 무겁다는 말은 b와 c는 동일하다는 의미
                return coins[0]
            elif coins[0] < coins[-1]:
                return coins[-1]
            else:  # a와 c가 같다면
                return coins[1]  # 나머지 b가 무겁다는 의미
        else:  # 3개의 동전이 남을 때까지 나눠진 동전 묶음에서 무거운 묶음을 찾아냄
            if sum(a) > sum(c):  # 동일한 개수로 동전을 나눴을 때 무게가 다른 것은 하나이므로 반드시 한 묶음의 무게는 차이가 발생
                return balance(a)
            elif sum(a) < sum(c):
                return balance(c)
            else:
                return balance(b)

    return problems.index(balance(problems)) + 1  # 편의상 인덱스 번호를 1번부터 시작


coins = 9
problems = [1.0] * coins
target = random.randrange(0, coins)  # 임의의 위치에 무거운 동전 생성

problems[target] = 1.1
print(problems)
print(solution(problems))
