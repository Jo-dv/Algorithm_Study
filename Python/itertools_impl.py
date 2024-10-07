arr = [1, 2, 3, 4]
n = 3


def c(idx, target, result):  # 리스트의 현재 인덱스, 선택된 수의 개수, 만들어지 조합
    if target == n:
        print(result)
        return
    if idx == len(arr):  # 숫자들이 다 선택되지 않은 상태에서 다음 숫자를 선택할 때 초과된 인덱스를 선택하는 것을 방지
        return
    c(idx + 1, target + 1, result + [arr[idx]])  # 현재 숫자 선택 후, 다음으로 넘어감
    c(idx + 1, target, result)  # 현재 숫자 선택 안 하고 다음으로 넘어감


def cr(idx, target, result):  # 중복 조합
    if target == n:
        print(result)
        return
    for i in range(idx, len(arr)):  # 수를 중복으로 표기할 땐 반복문을 사용
        cr(i, target + 1, result + [arr[i]])  # 반복문 범위가 배열의 범위이므로 인덱스를 체크할 필요 없음


def pt(target, result, visited):  # 순열
    if target == n:
        print(result)
        return
    for i in range(len(arr)):  # 반복문의 범위가 배열의 범위이므로 인덱스를 체크할 필요 없음
        if visited[i]:  # 이미 선택된 숫자라면 다음으로 넘어감
            continue
        visited[i] = True  # 현재 숫자 선택
        pt(target + 1, result + [arr[i]], visited)
        visited[i] = False


def pd(target, result):  # 중복 순열
    if target == n:
        print(result)
        return
    for i in range(len(arr)):  # 반복문의 범위가 배열의 범위이므로 인덱스를 체크할 필요 없음
        pd(target + 1, result + [arr[i]])


print("# 조합")
c(0, 0, [])
print("# 중복 조합")
cr(0, 0, [])
print("# 순열")
pt(0, [], [False] * len(arr))
print("# 중복 순열")
pd(0, [])
