def getPrimeList(n):
    seive = [True] * n

    for i in range(2,int(n**0.5)+1):
        if seive[i]:
            # 처음 소수의 다음 배수 부터 범위 지정
            for j in range(2*i,n,i):
                seive[j] = False

    return [i for i in range(2,n) if seive[i]]

def check(Sum, cnt, i):
    global ans
    if i >= len(nums): return
    if cnt == 3:
        if Sum == N: ans += 1
        return
    check(Sum+nums[i], cnt+1, i)
    check(Sum, cnt, i+1)

for tc in range(int(input())):
    N = int(input())
    ans = 0
    nums = getPrimeList(N)
    check(0,0,0)
    print("#%d %d" %(tc+1,ans))