T = int(input())

for i in range(1, T+1):
    N, k = map(int, input().split())
    table = []  # 학생들 성적을 기록할 list 생성
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']  # 학점표
    temp = [i for i in grade for _ in range(N//10)]  # 학생 수에 따른 학점표

    for student in range(1, N+1):
        mid, final, assignment = map(int, input().split())
        table.append((student, round(mid * 0.35 + final * 0.45 + assignment * 0.2, 2)))  # 학생의 번호와 성적 기록

    res = sorted([(j, k) for j, k in zip(sorted(table, key=lambda x: x[1], reverse=True), temp)], key=lambda x: x[0])
    # 성적을 내림차순으로 정렬 후, 학점을 부여하여 번호를 기준으로 오름차순으로 정렬하여 원래 학점표로 되돌림
    # 하나의 tuple로 합치기 위해 번호와 성적으로 된 tuple을 분해한 상태에서 학점을 부여하여 다시 하나의 tuple을 생성
    print(f'#{i} {res[k-1][1]}')
