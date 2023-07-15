k, score = 3, [10, 100, 20, 150, 1, 100, 200]

def solution(k, score):
    answer = []

    class node:  # 연결 리스트 풀이
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next

    head = node()

    for i in score:
        cnt, cur, prev = 0, head, None  # 삽입을 위한 커서 위치 초기화, 삽입마다 초기화 수행
        if cur.next is None:  # 연결 리스트에 데이터가 없다면, 커서는 헤드를 가리킴. 즉 cur.next -> head.next임
            head.next = node(i)  # 헤드에 노드를 생성하여 연결
        else:  # 노드가 하나 이상 있다면
            new_node = node(i)  # 새로운 노드 생성
            while cur.next is not None:  # 커서가 가리키는 노드의 다음이 마지막 노드가 아니라면
                if cur.next.data < i:  # 삽입할 데이터와 커서가 가리키는 다음 노드의 데이터보다 크다면
                    new_node.next = cur.next  # 새로운 노드를 커서가 가리키는 노드와 연결
                    prev = cur  # 커서의 정보를 저장했으므로 이전 노드를 커서 노드로 변경, 여기서 이전 노드는 새로운 노드의 직전 노드를 지칭
                    prev.next = new_node  # 이전 노드를 새로운 노드와 연결
                    break  # 삽입 종료
                else:  # 그렇지 않다면
                    cur = cur.next  # 커서를 갱신하며 삽입 노드의 위치 탐색
            if cur.next is None:  # 위치를 찾다가 커서가 가리키는 노드가 마지막 노드에 도달했을 때
                cur.next = new_node  # 노드 연결

        cur = head  # 마지막 순위에 있는 값을 저장하기 위해 커서 초기화
        while True:
            if cnt == k or cur.next is None:  # 커서가 마지막 노드를 가리키거나 노드의 위치가 k 번째일경우
                answer.append(cur.data)  # 해당 노드의 값 저장
                break
            cur = cur.next  # 위치를 찾을 때까지 커서를 갱신하며 탐색
            cnt += 1  # 탐색한 노드의 위치를 갱신

    return answer

print(solution(k, score))