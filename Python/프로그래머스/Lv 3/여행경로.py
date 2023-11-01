def dfs(graph, start, answer):
    end = graph.get(start, False)  # 도착 노드의 경우 딕셔너리에 존재하지 않으므로 기본값을 False로 처리

    while end:  # 그래프에 탐색할 노드가 있다면
        dfs(graph, end.pop(), answer)

    answer.append(start)


def solution(tickets):
    answer = []
    graph = dict()
    for f, t in tickets:
        if f not in graph:
            graph[f] = [t]
        else:
            graph[f].append(t)

    for i in graph.values():
        i.sort(reverse=True)
        # 알파벳 순으로 다음 선택지를 골라야하므로 -> dfs는 마지막 값이 먼저 들어오는 것을 반영해 역순 정렬

    dfs(graph, 'ICN', answer)

    return answer[::-1]  # dfs의 특성상 결과가 역순이므로 이를 뒤집어줌