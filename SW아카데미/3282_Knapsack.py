def knapsack(W,wt,val,n):
    K = [[0] * (W+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for w in range(1,W+1):
            if wt[i-1] <= w:
                K[i][w] = max(val[i-1]+K[i-1][w-wt[i-1]],K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]
for tc in range(int(input())):
    wt = []
    val = []
    N, K = map(int,input().split())
    for _ in range(N):
        v, c  = map(int,input().split())
        wt.append(v)
        val.append(c)
    print('#{} {}'.format(tc+1,knapsack(K,wt,val,N)))

def knapsack(W,wt,val,n): # W = 배낭의 무게한도, wt = 각 보석의 무게, val = 각 보석의 가격, n = 보석의 수

    K=[[0 for x in range(W+1)] for x in range(n+1)] #DP 담을 2차원 리스트
    for i in range(n+1):
        for w in range(W+1):
            if i ==0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]+K[i-1][w-wt[i-1]],K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K

for tc in range(int(input())):
    N, K = map(int, input().split())  # N = 개수 K = 물건의 부피한도
    wt = []  # 여기서는 각 물건의 부피
    val = [] # 각 물건의 가치
    Max = 0
    for _ in range(N):
        V, C = map(int, input().split())  # V = 부피 C = 가치
        wt.append(V)
        val.append(C)
    ans = knapsack(K,wt,val,N)
    print(ans)
