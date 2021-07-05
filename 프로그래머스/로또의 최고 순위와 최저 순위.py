'''
6개 1등
5개 2등
4개 3등
3개 4등
2개 5등
나머지 낙첨
'''
def check(num):
    if num == 6:
        return 1
    elif num == 5:
        return 2
    elif num == 4:
        return 3
    elif num == 3:
        return 4
    elif num == 2:
        return 5
    else:
        return 6

def solution(lottos, win_nums):
    answer = []
    cnt_zero = lottos.count(0)
    pos_cnt = 0
    for lo in lottos:
        if lo and lo in win_nums:
            pos_cnt += 1

    positive = cnt_zero + pos_cnt
    answer.append(check(positive))
    answer.append(check(pos_cnt))

    return answer
solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19])