from collections import deque

for _ in range(int(input())):
    p = input()
    n = int(input())
    arr = deque(input()[1:-1].split(','))
    # 괄호를 제거하여 숫자들만 추출해 큐 생성, []를 입력받으면 0번 인덱스에 '[]' 저장, 결과적으로 슬라이싱 범위에 벗어나 빈 큐가 됨
    flag = 1  # 뒤집기 여부

    for i in p:  # 함수를 하나씩 가져와서
        if i == 'R':  # 뒤집기일 경우
            flag *= -1  # 플래그 음수로 변환, R이 실행될 때마다 reverse() 수행할 필요 없이 플래그만 확인하면 됨
            continue  # 다음 명령어 호출
        if not arr or n == 0:  # 빈 리스트에서 데이터를 삭제할 경우
            print('error')  # 에러, 반복 종료
            break
        arr.pop() if flag == -1 else arr.popleft()  # 빈 리스트가 아닌 경우 뒤집어진 여부에 따라 값 제거
    else:  # 정상적으로 반복이 종료되었다면
        if flag == -1:  # 플래그가 음수라면 반대로 값을 출력하기 위해
            arr.reverse()  # 뒤집기
        print(f"[{','.join(arr)}]")  # 출력 형식에 맞춰서 출력
