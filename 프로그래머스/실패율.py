def solution(N, stages):
    answer = []
    cur_num = len(stages)
    res = []
    for i in range(1, N + 1):
        cnt = stages.count(i)
        if cur_num == 0:
            res.append((i, 0))
            continue
        res.append((i, cnt / cur_num))
        cur_num -= cnt
    res.sort(reverse=True, key=lambda data: data[1])

    for i in range(N):
        answer.append(res[i][0])
    return answer