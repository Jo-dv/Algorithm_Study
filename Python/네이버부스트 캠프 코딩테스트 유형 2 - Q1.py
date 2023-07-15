arr = [2, 3, 4, 4, 2, 5, 2, 5, 5]

def solution(arr):
    temp = {}

    for i in arr:
        if i not in temp:  # 데이터가 딕셔너리에 없다면
            temp[i] = 1  # 딕셔너리에 추가 후 값으로 1 부여
        else:  # 있다면
            temp[i] += 1  # 값 갱신

    res = [i for i in temp.values() if i > 1]  # 중복된 값인 것들만 추림
    return [-1] if len(res) == 0 else res  # 추린 값이 빈 리스트라면 [-1] 아니면 중복된 값의 개수를 순서대로 리스트에 출력

print(solution(arr))