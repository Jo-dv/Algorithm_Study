import string

msg = 'KAKAO'


def solution(msg):
    answer = []
    index = dict(zip(list(string.ascii_uppercase), range(1, 28)))  # 길이가 1인 모든 단어를 포함하도록 사전 초기화
    w = ''

    while msg:
        for c in msg:  # 현재 입력과 일치하는 가장 긴 문자열 탐색
            w += c  # 입력이 항상 영어 대문자이므로 시작 알파벳이 이미 사전에 있다는 것을 알 수 있다.
            if w not in index:  # 사전에 없는 단어를 찾아냈을 경우
                index[w] = len(index) + 1  # 사전에 추가
                break
        else:  # 해당 구문이 실행된다는 것은 더 이상 다음 문자가 없다는 것을 의미
            answer.append(index[msg])  # 마지막 문자(문자열)의 색인 저장
            break
        answer.append(index[msg[:len(w)-1]])  # 찾아낸 단어의 색인 저장
        msg = msg[len(w)-1:]  # 기존 문자열에서 찾아낸 문자열 제거
        w = ''  # 새로운 탐색을 위한 변수 초기화, 초기화하지 않으면 기존에 찾아낸 문자에 덧붙여짐

    return answer


print(solution(msg))
