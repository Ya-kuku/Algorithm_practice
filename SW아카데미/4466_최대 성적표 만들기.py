for tc in range(int(input())):
    N, K = map(int,input().split())
    score = list(map(int,input().split()))
    score.sort()
    score.reverse()
    print('#{} {}'.format(tc+1,sum(score[:K])))