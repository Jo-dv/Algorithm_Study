arr = [[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]

def solution(arr):
    answer = []
    termination = map(lambda x: len(x) == 1, arr)
    scale = len(arr)

    for i in range(scale):
        print(arr[i][:scale//2], end=' ')
        print(arr[i][scale // 2:])
    '''
    while not all(termination):
        for i in range(scale):
            print(arr[i][:scale // 2], end=' ')
            print(arr[i][scale // 2:])
        return'''
    return #[arr.count(0), arr.count(1)]

print(solution(arr))

