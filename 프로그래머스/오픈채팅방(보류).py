record = ["Enter uid1234 Muzi",
          "Enter uid4567 Prodo",
          "Leave uid1234",
          "Change uid4567 Ryan",
          "Enter uid1234 Prodo"]

def solution(record):
    answer = []
    log = [i.split() for i in record]
    reversed_log = [list(reversed(i.split())) for i in record]
    u_id = {i[1]: i[2] for i in log if len(i) == 3}

    for i, j in zip(log, reversed_log):
        if i[1] in u_id.keys():
            j[0] = u_id[i[1]]
        if j[1][0] == 'u':
            del j[1]
        if j[1] == 'Change':
            del j
        else:
            if j[1] == 'Enter':
                j[1] = '들어왔습니다.'
            if j[1] == 'Leave':
                j[1] = '나갔습니다.'
            answer.append(f'{j[0]}님이 {j[1]}')

    return answer

print(solution(record))