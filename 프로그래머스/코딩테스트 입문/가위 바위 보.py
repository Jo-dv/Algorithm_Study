rsp = '2'

def solution(rsp):
    answer = {'0': '5', '2': '0', '5': '2'}
    return ''.join([answer[i] for i in rsp])

print(solution(rsp))