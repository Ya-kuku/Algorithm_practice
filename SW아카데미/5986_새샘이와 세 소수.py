def getPrimeList(n):
    seive = [True] * n

    for i in range(2,int(n**0.5)+1):
        if seive[i]:
            # 처음 소수의 다음 배수 부터 범위 지정
            for j in range(2*i,n,i):
                seive[j] = False

    return [i for i in range(2,n) if seive[i]]

def check(Sum,n,cnt):
    global ans
    if Sum > n or cnt > 3:
        return

    if cnt == 3:
        if Sum == n:
            ans += 1
            return

    for i in range(len(nums)):
        check(Sum+nums[i],n,cnt+1)

for tc in range(int(input())):
    N = int(input())
    ans = 0
    nums = getPrimeList(N)
    check(0,N,0)
    print(ans)