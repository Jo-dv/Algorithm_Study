def solution(files):
    info = {i: None for i in range(len(files))}  # 분리한 데이터를 저장하기 위한 자료구조 생성

    for i, name in enumerate(files):
        h, n, t, flag = '', '', '', 1
        for c in name:  # 각 데이터에서 문자를 하나씩 가져와
            if not c.isdigit() and not n:  # 숫자가 아니고 숫자 데이터가 채워져 있지 않다면
                h += c  # 헤드
            elif c.isdigit() and len(n) < 6 and flag:  # 문자가 아닌 숫자 데이터고 아직 넘버의 길이가 5이하면서 아직 테일이 아닐 때
                n += c  # 넘버
            else:
                flag = 0  # 플래그를 false로 변환, 넘버의 길이가 5가 아니라도 테일에서 문자를 저장하다 갑자기 숫자가 나와 넘버에 저장되는 것을 방지
                t += c  # 테일
        info[i] = (h, n, t)  # 분할된 데이터를 튜플 형태로 저장

    res = list(info.values())  # 분할된 데이터들만 추출
    res.sort(key=lambda x: (x[0].lower(), int(x[1])))  # 헤드를 대소문자 상관없이 정렬하고 동일하다면 넘버순으로 정렬

    return [''.join(i) for i in res]  # 정렬된 튜플들을 하나의 문자열로 묶어 리스트에 저장 후 반환
    # 파이썬은 안정 정렬을 제공하므로 우선순위가 동일하다면 그것에 값 자체로 정렬하여 순서가 깨지는 것을 방지함, 즉 우선순위 다음은 값의 크기임

files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]

print(solution(files))