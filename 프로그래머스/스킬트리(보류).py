skill = 'CBD'
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

def solution(skill, skill_trees):
    answer = -1
    for i in skill_trees:
        temp = ''
        for j in i:
            if j in skill:
                temp += j
        print(temp)
    return answer

print(solution(skill, skill_trees))