skill, skill_trees = "BDC",["AAAABACA"]

def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees:
        info = {i: 100 for i in skill}  # 스킬의 순서를 기록할 딕셔너리 생성, 찍지 않은 값을 나타내기 위해 원소의 최대 길이보다 크게 설정
        for j in skill:  # 스킬순서에서 스킬을 하나씩 불러와
            if j in i:  # 내가 그 스킬 중에 하나를 찍었다면
                info[j] = i.index(j)  # 찍은 스킬의 순서를 기록
        x = list(info.values())  # 찍었던 스킬 순서 추출
        if x == sorted(x):  # 모든 스킬을 순서대로 찍었다면 순서는 오름 차순으로 구성됨
            answer += 1  # 스킬의 순서가 오름차순이라면 유효한 스킬

    return answer

print(solution(skill, skill_trees))