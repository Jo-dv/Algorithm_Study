n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]

def solution(n, arr1, arr2):
    answer = []
    enarr = [bin(x | y)[2:].zfill(n) for x, y in zip(arr1, arr2)]
    for i in enarr:
        i = i.replace('0', ' ')
        i = i.replace('1', '#')
        answer.append(i)
    return answer

print(solution(n, arr1, arr2))