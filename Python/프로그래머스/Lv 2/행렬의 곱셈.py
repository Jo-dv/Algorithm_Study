import numpy as np

arr1 = [[2, 3, 2],
        [4, 2, 4],
        [3, 1, 4]]

arr2 = [[5, 4, 3],
        [2, 4, 1],
        [3, 1, 1]]

def solution(arr1, arr2):
    #answer = np.dot(np.array(arr1), np.array(arr2)).tolist()
    answer = [[sum(x * y for x, y in zip(x, y)) for y in zip(*arr2)] for x in arr1]
    return answer

print(solution(arr1, arr2))