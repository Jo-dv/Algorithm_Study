numbers = '011'

def prime(n):
    p = [1 for _ in range(n + 1)]

    for i in range(2, int(n ** 0.5) + 1):
        if p[i]:
            for j in range(i ** 2, n + 1, i):
                p[j] = 0

    p = [i + 2 for i, j in enumerate(p[2:]) if j]
    return p

def dfs(numbers, path, result):
    if path:
        result.add(int(path))
    for i in range(len(numbers)):  # 선택되지 않은 숫자는 다음 탐색에, 선택된 숫자는 기존 경로에 붙여서 나중에 저장
        dfs(numbers[:i]+numbers[i+1:], path+numbers[i], result)

def solution(numbers):
    result = set()
    dfs(numbers, '', result)
    m = prime(max(result))
    return len([i for i in result if i in m])

print(solution(numbers))