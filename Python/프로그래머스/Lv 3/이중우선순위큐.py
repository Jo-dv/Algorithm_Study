from heapq import *

def solution(operations):
    minh, maxh = [], []
    for i in operations:
        o, d = i.split()
        if o == 'I':
            heappush(minh, int(d))
            heappush(maxh, -int(d))
        elif o == 'D':
            if d == '-1' and minh:
                heappop(minh)
            elif minh and maxh:
                if len(minh) == 1:  # 최소힙의 원소가 한 개 밖의 없으면 해당 값은 최소이면서 최대이기 때문에 제거해야 함
                    heappop(minh)
                heappop(maxh)

    h = set(minh) & set([-i for i in maxh])  # 최대힙을 만들 때 음수를 취해줬으므로 다시 원상복귀
    # 모든 힙에는 동일한 원소가 들어가고 최소힙의 길이가 1인 경우를 제외하고는
    # 최대값을 제거할 때만 최대힙에서 제거하고, 최소값을 제거할 때만 최초힙에서 제거한다.
    # 그렇기 양쪽 힙에 남아있는 동일한 값은 제거되지 않은 값들이다. 동일하지 않은 값은 어느쪽 큐에서 제거되었다는 의미
    return [0, 0] if not h else nlargest(1, h) + nsmallest(1, h)

'''
def solution(operations):  # 큰 차이는 없지만 굳이 최대값을 제거할 때마다 다시 힙으로 변환하는 것은 비효율적이라고 판단했음
    h = []
    for i in operations:
        o, d = i.split()
        if o == 'I':
            heappush(h, int(d))
        elif o == 'D' and h:
            if d == '-1':
                heappop(h) 
            else: 
                h.pop(h.index(nlargest(1, h)[0]))
                heapify(h)

    return [0, 0] if not h else [max(h), min(h)]
'''

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]

print(solution(operations))