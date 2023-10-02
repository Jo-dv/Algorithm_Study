record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    info = [i.split() for i in record]  # 문자열 데이터를 키워드별로 분리해서 다시 저장
    uid = {i[1]: i[2] for i in info if len(i) == 3}  # Leave를 제외하고 아이디와 닉네임 저장, 해당 반복을 통해 최종 닉네임이 저장됨

    return [f'{uid[i[1]]}님이 들어왔습니다.' if i[0] == 'Enter' else f'{uid[i[1]]}님이 나갔습니다.' for i in info if i[0] != 'Change']
    # Change를 제외하고 각 명령에 따라 유저 아이디에 맞는 닉네임을 불러와 응답 처리

print(solution(record))