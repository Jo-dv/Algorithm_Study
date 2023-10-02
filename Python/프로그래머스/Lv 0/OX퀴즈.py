quiz = ["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]

def solution(quiz):
    # return ['O' if eval(i[0]) == eval(i[1]) else 'X' for i in [i.split('=') for i in quiz]]
    # eval()은 문자열로 표현된 코드를 실행하여 결과를 반환하는 함수, 만약 서버에 접근하여 정보를 가져오는 코드를 집어 넣을 경우, 보안 이슈 발생
    answer = []
    for i in [i.split('=') for i in quiz]:
        for j in i[:-1]:
            j = j.split()
            if j[1] == '+':
                answer.append('O') if int(j[0]) + int(j[2]) == int(i[-1]) else answer.append('X')
            else:
                answer.append('O') if int(j[0]) - int(j[2]) == int(i[-1]) else answer.append('X')
    return answer

print(solution(quiz))