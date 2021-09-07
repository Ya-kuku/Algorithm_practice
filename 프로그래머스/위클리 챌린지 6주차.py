def solution(weights, head2head):
    answer = []
    n = len(weights)
    for i in range(n):
        victory = 0
        win_weight = 0
        cnt = 0
        for j in range(n):
            if i == j: continue
            if not head2head[i][j] == 'N': cnt += 1
            if head2head[i][j] == 'W': victory += 1
            if head2head[i][j] == 'W' and weights[i] < weights[j]: win_weight += 1
        if cnt == 0:
            victory = 0
        else:
            victory = victory / cnt
        answer.append([victory,win_weight,weights[i],i])
    answer.sort(key=lambda data : (-data[0],-data[1],-data[2],data[3]))
    res = [a[3]+1 for a in answer]
    print(answer)
    return res

solution([60,70,60],["NNN","NNN","NNN"])