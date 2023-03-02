num_list = [1, 2, 3, 4, 5]

def solution(num_list):
    return [len([i for i in num_list if i % 2 == 0]), len([i for i in num_list if i % 2 != 0])]

print(solution(num_list))