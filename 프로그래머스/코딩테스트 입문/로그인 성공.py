id_pw, db = ["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]

def solution(id_pw, db):
    info = {id: pw for id, pw in db}
    try:  # 아래 코드는 키가 있다면 반드시 실행됨, 그렇기에 비번만 비교하면 됨
        return 'login' if info[id_pw[0]] == id_pw[1] else 'wrong pw'
    except KeyError:  # 키 자체가 없다는 것은 일치하는 정보가 없다는 의미
        return 'fail'

print(solution(id_pw, db))