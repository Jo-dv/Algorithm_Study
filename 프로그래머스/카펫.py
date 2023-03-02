brown = 18
yellow = 6

def solution(brown, yellow):
    temp = [i for i in range(1, brown + yellow + 1) if (brown + yellow) % i == 0]
    # brown + yellow는 카펫의 넓이와도 같다. 카펫의 너비와 높이는 넓이의 약수로 나타낼 수 있다.

    if len(temp) % 2 == 0:  # 약수의 개수가 짝수일 경우
        for h, w in zip(temp[:len(temp)//2], temp[:len(temp)//2-1:-1]):  # 투 포인터 방식으로 양쪽 끝에서 값을 탐색
            # w >= h를 만족하므로 h, w 형태로 값을 표현
            if w + h == (4 + brown) // 2:  # 해당 식을 만족할 경우
                return [w, h]
    else:
        return [temp[len(temp)//2]]*2  # 홀수일 경우 항상 가운데 약수의 페어로 표현 가능하다.

# 해를 만족하는지 확인하는 식은 다음과 같다.
# (w-2)(h-2) = yellow
# wh-2(w+h) = yellow-4
# wh = brown + yellow
# brown + yellow = 카펫의 넓이가 성립하는 이유는 모든 격자를 일렬로 펼치면 높이 1, 너비 b+y가 되기 때문에 넓이는 b+y가 된다.
print(solution(brown, yellow))