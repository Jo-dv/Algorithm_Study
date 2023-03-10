from collections import deque

A, B = 'hello', 'ohell'

def solution(A, B):
    deque_A = deque(A)
    for i in range(len(deque_A)):
        if B == ''.join(deque_A):
            return i
        deque_A.rotate()
    else:
        return -1

print(solution(A, B))