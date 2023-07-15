s = "110010101001"

def solution(s):
    temp = []
    count = length = 0

    while s != '1':
        for i in s:
            if i == '1':
                temp.append(i)

        length += len(s) - len(temp)
        s = bin(len(temp))[2:]
        temp = []
        count += 1

    return [count, length]

print(solution(s))