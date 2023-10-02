elements = [7,9,1,1,4]

'''
def solution(elements):
    x = len(elements)
    for i in range(x, 2 * x - 2):
        # 순환되는 수열의 길이의 최대는 총 길이-1, 마지막 인덱스를 시작번호로 했을 때 필요한 인덱스는 len+(len-2)
        elements.append(elements[i % x])  # 순환 인덱스
    return len(set(sum(elements[j:j+i]) for j in range(x) for i in range(1, x)))+1  # 총 길이만큼 순회하는 것은 모두 같으므로 +1
'''

def solution(elements):  # 속도 약 10배 개선
    answer = set()
    for i in range(len(elements)):  # 규칙성을 보면 반복이 될 때마다 다음에 숫자가 붙는 구조 확인 가능
        temp = 0
        for j in range(i, len(elements)+i-1):  # -1을 해줌으로써 총 길이만큼 순회하지 않도록 함
            temp += elements[j%len(elements)]  # 매 반복마다 처음 인덱스에 마지막까지 순회하여 하는 sum보다 훨씬 효율적
            answer.add(temp)
    return len(answer)+1

print(solution(elements))