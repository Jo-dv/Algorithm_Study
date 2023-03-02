money = 15000

def solution(money):
    amount, change = divmod(money, 5500)
    return [amount, change]

print(solution(money))
