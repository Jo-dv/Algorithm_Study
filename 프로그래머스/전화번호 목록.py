from collections import Counter

phone_book = ["119", "97674223", "1195524421"]

def solution(phone_book):
    answer = True
    hash = dict.fromkeys(phone_book)

    for i in hash:
        temp = ''
        for j in i:
            temp += j
            if temp in hash and temp != i:
                answer = False

    return answer

print(solution(phone_book))
