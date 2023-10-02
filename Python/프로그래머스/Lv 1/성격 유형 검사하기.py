survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]


def solution(survey, choices):
    characters = {key: 0 for data in ["RT", "CF", "JM", "AN"] for key in data} # 지표별로 유형 분리
    answer = ''

    for i in range(len(survey)):
        if choices[i] < 4: # 응답 값이 4보다 작으면 비동의
            characters[survey[i][0]] += abs(4 - choices[i]) # 값 스케일링
        if choices[i] > 4: # 응답 값이 4보다 크면 동의
            characters[survey[i][1]] += abs(4 - choices[i]) # 값 스케일링

    l_d = list(characters.items()) # 편의상 리스트로 변환
    for i in range(0, len(l_d), 2): # 지표가 2개로 이루어져 있으므로 2개씩 짝지어 비교
        if l_d[i][1] > l_d[i + 1][1]: # 지표의 첫 번째 응답 값이 클 경우 해당 지표 선택
            answer += l_d[i][0]
        elif l_d[i][1] == l_d[i + 1][1]: # 지표의 각 응답 값이 모두 같을 경우 알파벳 순으로 지표 선택, 이미 주어진 지표는 알파벳 순으로 이루어짐
            answer += l_d[i][0] # 그래서 첫 번째, 첫 조건에 삽입하지 않은 이유는 이해하기 편하라고
        else:
            answer += l_d[i + 1][0] # 지표의 두 번째 응답 값이 클 경우 해당 지표 선택

    return answer


print(solution(survey, choices))
