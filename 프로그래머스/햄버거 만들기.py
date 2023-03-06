ingredient = [2, 1, 1, 2, 1, 2, 3, 1, 1]


# 햄버거 만드는 순서: 1, 2, 3, 1
def solution(ingredient):
    i, answer = 0, 0

    while i < len(ingredient) - 3:  # 탐색 인덱스가 리스트의 최소 인덱스를 넘어설 경우 종료
        # len - 3인 이유는 len이 최소 4일 때 탐색을 한 번은 해야하므로
        if ingredient[i:i + 4] == [1, 2, 3, 1]:  # 슬라이딩 윈도우 형식으로 4칸씩 확인
            del ingredient[i:i + 4]  # 확인되면 해당 데이터 제거
            answer += 1  # 결과 갱신
            i -= 4  # 다음에 인덱스가 하나 갱신할 것을 고려해 현재 위치에서 -4 이동, 결과적으로 -3만큼 이동하는 꼴
            # -3칸 이동해야 삭제하고 남은 인덱스를 마지막 네 번째 값으로 하여 결과를 다시 비교할 수 있음
            # 2 1 1 2 [1 2 3 1] 3 1
            # 2 1 [1 1 2 3] 1
        i += 1  # 탐색 인덱스를 다음으로 갱신

    return answer


print(solution(ingredient))
