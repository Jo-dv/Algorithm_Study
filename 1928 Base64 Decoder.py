en_table = {i - 65: chr(i) for i in range(ord('A'), ord('Z') + 1)}
for j in range(ord('a'), ord('z') + 1):
    en_table[j - 71] = chr(j)
for j in range(10):
    en_table[j + 52] = str(j)
en_table[62], en_table[63] = '+', '/'  # encoding table, 0: 'A', 1: 'B', ... , 62: '+', 63: '/'
de_table = {v: k for k, v in en_table.items()}  # decoding table, 'A': 0, 'B': 1, ... , '+': 62, '/': 63


def encoder(table, data):
    t, encoding = '', ''
    for i in data:  # 입력받은 문자열에서 문자를 하나씩 분리
        t += bin(ord(i))[2:].zfill(8)
        # 분리된 문자를 ASCII 값으로 변경 후, 8자리 이진수로 변환하여 한 줄로 합침, 8자리가 되도록 앞에서 0을 채움
    for i in range(0, len(t), 6):  # 하나로 합쳐진 data를 6자리씩 끊어서
        encoding += table[int(t[i:i + 6], 2)]  # 끊긴 6자리 이진수를 ASCII 값으로 변환, 해당 값을 key로 가지는 value로 encoding
    return encoding


def decoder(table, data):
    d, decoding = '', ''  # encoding 순서를 반대로 수행
    for i in data:  # encoding된 data를 받아서 하나씩 분리
        d += bin(table[i])[2:].zfill(6)
        # 분리된 문자의 값을 찾아, encoding의 마지막 단계에서 6자리씩 끊었으므로 6자리 이진수로 변환하여 한 줄로 합침
    for i in range(0, len(d), 8):  # 하나로 합쳐진 data를 8자리씩 끊어서
        decoding += chr(int(d[i:i + 8], 2))  # 끊긴 8자리 이진수를 ASCII 값으로 변환, 해당 값에 상응하는 문자로 변환
    return decoding


T = int(input())
for i in range(1, T+1):
    print(f'#{i} {decoder(de_table, input())}')
