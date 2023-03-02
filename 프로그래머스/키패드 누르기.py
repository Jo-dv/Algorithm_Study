numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"


def solution(numbers, hand):
    answer = ''
    keypad = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              ['*', 0, '#']]
    L_hand = '*'
    R_hand = '#'
    for number in numbers:
        if number in list(zip(*keypad))[0]:
            L_hand = number
            answer += 'L'

        if number in list(zip(*keypad))[1]:
            L = sum([list((i, j)) for i in range(4) for j in range(3) if keypad[i][j] == L_hand], [])
            R = sum([list((i, j)) for i in range(4) for j in range(3) if keypad[i][j] == R_hand], [])
            target = sum([list((i, j)) for i in range(4) for j in range(3) if keypad[i][j] == number], [])
            L_Distance = sum([abs(i - j) for i, j in zip(L, target)])
            R_Distance = sum([abs(i - j) for i, j in zip(R, target)])

            if L_Distance > R_Distance:
                R_hand = number
                answer += 'R'
            elif L_Distance == R_Distance:
                if hand == 'L_hand':
                    L_hand = number
                else:
                    R_hand = number
                answer += hand[0].upper()
            else:
                L_hand = number
                answer += 'L'

        if number in list(zip(*keypad))[2]:
            R_hand = number
            answer += 'R'

    return answer


print(solution(numbers, hand))
