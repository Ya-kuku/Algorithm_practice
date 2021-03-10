def solution(clothes):
    answer = {}
    ans = 1
    for i in clothes:
        if i[1] in answer: answer[i[1]] += 1
        else: answer[i[1]] = 1
    for i in answer.values():
        ans *= (i+1)
    return ans - 1