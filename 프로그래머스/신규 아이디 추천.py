id = "abcdefghijklmn.p"

def solution(new_id):
    identifier = ['-', '_', '.']
    new_id = new_id.lower()
    new_id = ''.join([i for i in new_id if i.isalpha() or i.isdecimal() or i in identifier])
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    new_id = new_id.strip('.')
    new_id = ''.join(['a' if not new_id else new_id])
    new_id = ''.join([new_id[:15] if len(new_id) >= 16 else new_id])
    new_id = ''.join([new_id.rstrip('.') if new_id[-1] == '.' else new_id])
    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id

print(solution(id))