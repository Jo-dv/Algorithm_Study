num_list, n = [1, 2, 3, 4, 5, 6, 7, 8], 2

def solution(num_list, n):
    return [num_list[i:i+n] for i in range(0, len(num_list), n)]

print(solution(num_list, n))