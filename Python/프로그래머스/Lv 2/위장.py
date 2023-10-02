clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"],
           ["red_sunglasses", "eyewear"], ["green_sunglasses", "eyewear"], ["crow_mask", "face"]]

def solution(clothes):
    table = {key[1]: 0 for key in clothes}
    for i in clothes:
        table[i[1]] += 1

    answer = 1
    for i in table.values():
        answer *= i+1
        # +1은 해당 아이템을 입지 않는 경우의 수, 헤드기어의 종류가 2개(a, b)라면 하나만 착용할 수 있으므로 둘 다 착용을 안 하거나
        # a만 착용하거나 b만 착용하거나 총 3개의 경우의 수 존재

    return answer - 1 # 아이템을 아예 안 입는 경우는 없지만 해당 경우의 수도 같이 카운트했기 때문에(공집합) -1

print(solution(clothes))