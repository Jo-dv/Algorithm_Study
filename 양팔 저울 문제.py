import random


def solution(problems):
    def balance(coins):
        idx1 = len(coins) // 3
        idx2 = len(coins) // 3 * 2
        idx3 = len(coins)

        A = coins[0:idx1]; B = coins[idx1:idx2]; C = coins[idx2:idx3]

        if len(coins) == 3:
            if coins[0] > coins[-1]:
                return coins[0]
            elif coins[0] < coins[-1]:
                return coins[-1]
            else:
                return coins[1]
        else:
            if sum(A) > sum(C):
                return balance(A)
            elif sum(A) < sum(C):
                return balance(C)
            else:
                return balance(B)

    return problems.index(balance(problems)) + 1


coins = 9
problems = [1] * coins
target = random.randrange(0, coins)

problems[target] = 1.1
print(problems)
print(solution(problems))
