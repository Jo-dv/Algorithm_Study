import re
from collections import Counter

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
modified_info = []
modified_query = []
infos = []
queries = []
result = []

for x, y in zip(info, query):
    modified_info.append(x.split())
    y = re.sub('and', '', y)
    modified_query.append(y.split())

for i in range(len(modified_info[0])):
    infos.append({'lang': modified_info[i][0], 'job': modified_info[i][1], 'career': modified_info[i][2],
                  'food': modified_info[i][3], 'score': modified_info[i][4]})
    queries.append({'lang': modified_query[i][0], 'job': modified_query[i][1], 'career': modified_query[i][2],
                  'food': modified_query[i][3], 'score': modified_query[i][4]})
