m = 12
d = 24


# 29: 2
# 30: 4, 6, 9, 11
# 31: 1, 3, 5, 7, 8, 10, 12

def solution(a, b):
    month = 1
    day = 1
    days = {4: 'MON', 3: 'TUE', 2: 'WED', 1: 'THU', 0: 'FRI', 6: 'SAT', 5: 'SUN'}
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while month != a:
        if day + 7 > months[month-1]:
            day += 7 - months[month-1]
            month += 1
        day += 7
    return days[(day - b) % 7]

print(solution(m, d))
