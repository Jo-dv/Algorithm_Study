test_case = [
    ['BOOL', 'BOOL'],
    ['BOOL', 'SHORT'],
    ['BOOL', 'FLOAT'],
    ['BOOL', 'SHORT', 'FLOAT'],
    ['BOOL', 'INT'],
    ['SHORT', 'BOOL'],
    ['FLOAT', 'SHORT'],
    ["INT", "INT", "BOOL", "SHORT", "LONG"],
    ["INT", "SHORT", "FLOAT", "INT", "BOOL"],
    ["FLOAT", "SHORT", "BOOL", "BOOL", "BOOL", "INT"],
    ["BOOL", "LONG", "SHORT", "LONG", "BOOL", "LONG", "BOOL", "LONG", "SHORT", "LONG", "LONG"]
]

output = [
    "'##......'",
    "'#.##....'",
    "'#...####'",
    "'#.######'",
    "'#.......,########'",
    "'###.....'",
    "'######..'",
    "'########,########,#.##....,########,########'",
    "'########,##..####,########,#.......'",
    "'########,#.......,########'",
    "'HALT'"
]


def solution(param0):
    answer = []
    info = {'BOOL': 1, 'SHORT': 2, 'FLOAT': 4, 'INT': 8, 'LONG': 16}
    total_size = 0
    start = 0
    slot = ['.'] * 8

    for param in param0:
        total_size += 8 if info[param] < 16 else info[param]  # 메모리 할당, LONG 타입은 8x2 나머지는 8 만큼의 메모리를 할당
        if total_size > 128:  # 할당된 전체 메모리의 크기가 제한 범위를 넘길 경우
            return "'HALT'"
        if start != 0 and ((info[param] == 2 and start % 2 != 0) or (info[param] == 4 and start % 4 != 0)):
            start = info[param]  # 배수가 되는 위치를 시작 위치로 지정
            # 데이터가 처음 저장되는 것이 아니며 SHORT나 FLOAT 타입의 데이터라면 해당 데이터 크기의 배수가 되는 위치부터 할당되야 함
        if start + info[param] - 1 >= 8:  # 데이터가 저장될 메모리의 시작 위치가 범위(0 ~ 7)를 초과했을 경우
            if slot != ['.'] * 8:  # 현재 메모리가 빈 메모리가 아니라면
                answer.append(''.join(slot))  # 해당 메모리 저장
                start = 0  # 현재 입력으로 들어온 데이터를 저장하기 위해 시작 위치 초기화
                slot = ['.'] * 8  # 새로운 메모리 할당
            if info[param] == 16:  # 들어온 데이터가 LONG 타입이라면
                answer.append('#' * 8)
                answer.append('#' * 8)
                continue  # 이미 데이터를 메모리에 할당했으므로 데이터를 추가하는 아래의 코드들이 실행될 필요가 없음
        for i in range(start, start + info[param]):  # 시작 위치부터 데이터의 크기만큼
            slot[i] = '#'
        start += info[param]  # 다음 데이터가 저장되는 메모리의 시작 위치는 현재 저장된 데이터의 타입만큼, 즉 데이터의 끝 바로 다음
    else:
        if slot != ['.'] * 8:  # 마지막 메모리가 빈 메모리가 아니라면
            answer.append(''.join(slot))

    return "'" + str(answer).replace(' ', '').replace("'", '')[1:-1] + "'"


for t, o in zip(test_case, output):
    ans = solution(t)
    print(ans == o, solution(t))