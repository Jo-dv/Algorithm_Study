price = 580000

def solution(price):
    if price < 100000:
        price * 1
    elif 100000 <= price < 300000:
        price *= 0.95
    elif 300000 <= price < 500000:
        price *= 0.9
    else:
        price *= 0.8
    return int(price)

print(solution(price))