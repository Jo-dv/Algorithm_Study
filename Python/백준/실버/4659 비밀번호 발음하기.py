def solve():
    while True:
        test_case = input()
        if test_case == "end":
            break

        flag1 = flag2 = flag3 = True
        cnt0 = cnt1 = cnt2 = 0

        for i in test_case:
            if i in ['a', 'e', 'i', 'o', 'u']:  # 모음을 포함하는지
                cnt0 += 1  # 모음이라면
                cnt2 = 0  # 현재 문자가 모음이라면 지금까지 기록된 자음의 수 초기화
                cnt1 += 1  # 모음이 연속적인지 확인하는 변수
                if cnt1 >= 3:  # 모음이 연속적으로 3개 이상이라면
                    flag2 = False
            else:
                cnt1 = 0  # 현재 문자가 자음이라면 지금까지 기록된 모음의 수 초기화
                cnt2 += 1  # 자음이 연속적인지 확인하는 변수
                if cnt2 >= 3:  # 자음이 연속적으로 3개 이상이라면
                    flag2 = False
        if cnt0 == 0:  # 모음의 수가 0이라면
            flag1 = False

        for i in range(len(test_case) - 1):  # 두 글자씩 확인
            if test_case[i] == test_case[i + 1] and test_case[i] + test_case[i + 1] not in ["ee", "oo"]:
                flag3 = False  # 두 글자가 같으면서 주어진 조건의 문자가 아니라면
                break

        print(f'<{test_case}> ' + ("is acceptable." if flag1 and flag2 and flag3 else "is not acceptable."))


solve()
