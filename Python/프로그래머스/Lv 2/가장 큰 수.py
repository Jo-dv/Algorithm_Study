numbers = [6, 10, 2]

def solution(numbers):
    return '0' if sum(numbers) == 0 else ''.join(sorted(list(map(str, numbers)), key=lambda x: str(x)*3, reverse=True))
    # 숫자로 된 문자열은 정렬 기준이 각 자리의 아스키 코드이다. 1000은 값 비교에서 항상 뒤에 오기에 최대 자릴수를 세 자리로 볼 수 있다.
    # 그렇기에 모든 문자열에 3을 곱하여 최소 세 자리의 문자로 만들어 주어 각 자리에 아스키 값을 비교하여 정렬한다.

'''
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer
    
    # func() 함수는 두 개의 인수를 입력하여 첫 번째 인수를 기준으로 그 둘을 비교하고 작으면 음수, 같으면 0, 크면 양수를 반환하는 비교 함수
    # 리턴은 위와 같이 고정하되 비교 기준, 즉 정렬 기준은 자유롭게 작성 가능 
'''

print(solution(numbers))