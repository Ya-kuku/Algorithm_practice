from itertools import permutations
def check(user,ban):
    for i in range(len(ban)):
        # 후보군 아이디 중 ban 아이디와 길이 다른 경우
        if len(user[i]) != len(ban[i]):
            return False
        # 길이가 같은 후보군 아이디 검사
        for j in range(len(user[i])):
            if ban[i][j] == '*':
                continue
            if ban[i][j] != user[i][j]:
                return False

    return True

def solution(user_id, banned_id):
    answer = []
    user_list = list(permutations(user_id,len(banned_id)))

    for user in user_list:
        if check(user,banned_id):
            print(sorted(user))
            ans = sorted(user)
            if ans not in answer:
                answer.append(ans)

    return len(answer)

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"])