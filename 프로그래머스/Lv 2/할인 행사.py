from collections import Counter

def solution(want, number, discount):
    answer = 0
    info = dict(zip(want, number))  # 원하는 품목과 수량을 하나로 묶음

    for i in range(len(discount) - 9):  # 전체 할인 기간 - 회원 유지 기간 + 당일, 제시된 기간 중 유지기간이 마지막 날까지만 계산하면 됨
        if info == Counter(discount[i:i+10]):  # 가입 날짜 기준 할인 품목과 비교
            answer += 1

    return answer

'''
def solution(want, number, discount):  # 카운터를 사영하지 않는 풀이
    answer = 0
    info = dict(zip(want, number))
    
    for i in range(len(discount)):
        check = {i: 0 for i in want}
        for j in want:
            check[j] += discount[i:i+10].count(j)
        if info == check:
            answer += 1

    return answer
'''



want, number = ["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork",
            "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

print(solution(want, number, discount))