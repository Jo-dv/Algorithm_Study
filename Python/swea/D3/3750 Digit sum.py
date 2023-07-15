temp = []

for _ in range(1, int(input())+1):  # sys.stdin.stdin.readline().rstrip()을 사용 못하는 경우
    temp.append(sum(list(map(int, input()))))  # 입력받은 문자열을 정수형 리스트로 변환 후, 합산
    # 입력의 경우 입력 횟수나 입력 데이터의 크기에 영향을 받기 때문에, 제약사항이 빡빡하다면 따로 처리해야 함

for i in range(len(temp)):
    x = temp[i]  # 저장된 합산 데이터를 하나씩 가져와서
    while len(str(x)) > 1:  # 문자열로 변환했을 때 길이가 1이 될 때까지
        x = sum(list(map(int, str(x))))
        # 정수형 리스트로 변환해서 합산하는 작업을 반복, 정수형 리스트를 만들기 위해선 정수를 문자열로 바꿔줘야 함

    print(f'#{i+1} {x}')