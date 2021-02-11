N,M = map(int,input().split())
cards = list(map(int,input().split()))

# Max = 0
# ans = 0
# for i in range(len(cards)):
#     for j in range(i+1,len(cards)):
#         for k in range(j+1,len(cards)):
#             ans = cards[i] + cards[j] + cards[k]
#             if ans > Max and ans <= M:
#                 Max = ans
#
# print(Max)

def check(cnt,cards,ans):
    global Max
    if ans > M:
        return
    if cnt == 3:
        if ans > Max:
            Max = ans
        return

    for i in range(N):
        if not visit[i]:
            visit[i] = True
            ans += cards[i]
            check(cnt+1,cards,ans)
            visit[i] = False
            ans -= cards[i]

visit = [0] * N
Max = 0
check(0,cards,0)
print(Max)
