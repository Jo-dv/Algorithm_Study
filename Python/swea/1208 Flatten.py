for i in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(dump):
        high = boxes.index(max(boxes))  # 최고점의 위치
        low = boxes.index(min(boxes))  # 최저점의 위치
        boxes[high] -= 1  # 최고점의 상자를 하나 빼서
        boxes[low] += 1  # 최저점으로 옮김
    print(f'#{i} {max(boxes)-min(boxes)}')  # dumping이 완료되면 최고점과 최저점의 차이를 반환