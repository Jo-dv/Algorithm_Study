numbers = [3, 30, 34, 301, 5, 9]

def solution(numbers):
    if sum(numbers) == 0:
        return '0'
    else:
        numbers = list(map(str, numbers))
        print(numbers)
        numbers.sort(key=lambda x: (-int(x[0]), -int(x[-1], len(x))))
        print(numbers)
        return ''.join(numbers)

print(solution(numbers))