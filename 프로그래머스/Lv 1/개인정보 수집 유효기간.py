today, terms, privacies ="2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

def solution(today, terms, privacies):
    dic, answer = {i[0]: [] for i in terms}, []

    for idx, i in enumerate(privacies):  # 약관 별로 수집 일자 분류
        data, t = i.split()
        x = list(map(int, data.split('.'))) + [idx+1]  # 일자를 분리하여 정수로 변환하여 저장, 추후 결과 반환을 위해 마지막에 인덱스 추가
        x[2] = 28 if x[2] == 1 else x[2]-1  # day가 1일이면 28일로, 그렇지 않으면 전날로 변환
        dic[t].append(x)  # 변환된 일자 저장
        
    for i in terms:
        t, p = i.split()  # 약관과 유효기간 분리
        for j in dic[t]:  # 약관별 일자 호출
            m = j[1] + (int(p)%12) - (0 if j[2] != 28 else 1)  
            # 현재 일자와 약관을 합하여 종료 일자의 달을 계산, 일이 28이면 유효기간에서 -1을 해준다. 4주를 기준으로 계산하므로 1일에 계약하면 달이 넘어가지 않고 마지막 날인 28일이 된다. 
            # 12로 나눠 나머지를 더하는 이유는 유효기간이 12의 배수이면 달 자체에는 영향을 주지 않기 때문
            j[0] += (int(p)//12) + m // (12 if m > 12 else 13)  
            # 유효기간에서 연도에만 영향을 주는 것을 계산, 유효기간과 계산할 달이 12달을 넘길 경우 몇년의 변화가 생기는지를 합하여 계산
            j[1] = m % (12 if m > 12 else 13)
            # 계산할 달이 12를 넘어가면 몇월이 되는지 계산. 12를 12로 나누면 0이 되기 때문에 13으로 나누는 것, 위에 식도 마찬가지
            answer.append(j)  # 계산된 종료 일자 저장

    today = list(map(int, today.split('.')))  # 결과 비교를 위해 변환
    answer.sort(key=lambda x: x[-1])  # 종료 일자를 원래의 인덱스 순으로 정렬
    return [i+1 for i, j in enumerate(answer)
            if today[0] > j[0] or # 종료 일자의 연도가 오늘 날짜의 연도보다 작거나 연도는 같은데 월이 작거나 연월은 같은데 날짜가 작다면
            (today[0] == j[0] and today[1] > j[1]) or
            (today[0] == j[0] and today[1] >= j[1] and today[2] > j[2])]

print(solution(today, terms, privacies))