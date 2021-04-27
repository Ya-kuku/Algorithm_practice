# 본인, 추천인, 판매자, 그 판매자가 판 수량
def solution(enroll, referral, seller, amount):
    result = {name: 0 for name in enroll}

    p = dict()  # 부모 정보 (추천인)
    for i in range(len(enroll)):
        p[enroll[i]] = referral[i]
    p['-'] = '-'

    for i in range(len(seller)):
        dadangye = amount[i]*100
        people = seller[i]
        while people != p[people] and dadangye > 0:
            result[people] += dadangye - dadangye//10
            dadangye //= 10
            people = p[people]

    ans = []
    for name in enroll:
        ans.append(result[name])

    return ans