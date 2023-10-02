price = 3
money = 20
count = 4

def solution(price, money, count):
    res = 0
    for i in range(1, count + 1):
        res += price * i

    if res > money:
        return res - money
    else:
        return 0

print(solution(price, money, count))