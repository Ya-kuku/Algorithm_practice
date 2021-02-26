def check_prime(n):
    seive = [True] * (n+1)
    for i in range(2,int(n**(0.5)+1)):
        if seive[i]:
            for j in range(2*i,n+1,i):
                seive[j] = False

    return[i for i in range(2,n+1) if seive[i]]
for tc in range(int(input())):
    D,A,B = map(int,input().split())

    nums = check_prime(B)
    print(nums)
    ans = 0
    for num in nums:
        if num >= A and str(D) in str(num):
            ans += 1
    print('#{} {}'.format(tc+1,ans))
