s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"


def solution(s):
    answer = []
    temp = []
    s = s[2:-2].split('},{')  # 양측 2개의 중괄호를 건너뛰고 split을 이용해 숫자들만 뽑아냄

    for i in s:  # 뽑아낸 숫자들이 문자열이기 때문에 중괄호가 없어도 하나의 덩어리로 묶임
        temp.append(set(i.split(',')))  # 묶인 덩어리를 split으로 분리하여 집합으로 변환
    temp.sort(key=len)
    # {{a1}, {a1, a2}, {a1, a2, a3}, {a1, a2, a3, a4}, ... {a1, a2, a3, a4, ..., an}}의 규칙을 가지므로 길이를 기준으로 정렬

    for i in temp:  # 리스트 안에 집합이 들어있으므로
        for j in i:  # 집합의 값들을 가져와서
            if j not in answer:  # 정답 리스트에 존재하지 않으면 해당 값을 추가, 즉 중복 방지
                answer.append(j)

    return list(map(int, answer))  # 출력이 정수형 리스트이므로 문자열 데이터를 정수로 매핑


print(solution(s))
