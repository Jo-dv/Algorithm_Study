num_set = input()
check = [0] * 10

for i in num_set:
    num = int(i)
    if num in [6, 9]:  # 6과 9만 고려하면 됨, 6과 9는 0.5 세트로 간주
        idx = min((check[6], 6), (check[9], 9))[1]  # 해당 인덱스 중 값이 작은 인덱스를 찾아서 값 갱신
        check[idx] += 1
    else:  # 나머지 숫자는 고유 숫자로 카운팅 된 수만큼의 세트가 필요
        check[num] += 1

print(max(check))