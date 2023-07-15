T = int(input())

num_system = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}

for i in range(1, T+1):
    t_num, t_len = input().split()
    t = input().split()

    print(f'#{i}', *sorted(t, key=lambda x: num_system[x]))  # 주어진 문자열의 key 값을 기준으로 오름차순 정렬