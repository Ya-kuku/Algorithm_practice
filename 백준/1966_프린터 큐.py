for tc in range(int(input())):
    # N문서 개수, M 문서 위치
    N, M = map(int,input().split())
    file = list(map(int,input().split()))
    score = []
    # score = [(idx,i) for idx, i in enumerate(file)]
    for idx, value in enumerate(file):
        score.append((idx,value))
    Max = max(score, key=lambda x:x[1])
    # print(Max)
    ans = 0
    while score:
        tmp = score.pop(0)
        if tmp[0] == M and tmp[1] == Max[1]:
            ans +=1
            break
        elif tmp[1] == Max[1]:
            ans += 1
            Max = max(score, key=lambda x: x[1])
        else:
            score.append(tmp)
    print(ans)

