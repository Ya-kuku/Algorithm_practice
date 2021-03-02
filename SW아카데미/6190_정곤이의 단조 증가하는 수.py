for tc in range(int(input())):
    N = int(input())
    nums= list(map(int,input().split()))

    ans = -1

    for i in range(1,len(nums)-2):
        for j in range(1+i,len(nums)-1):
            tmp = nums[i] * nums[j]
            tmp = str(tmp)
            for k in range(1,len(tmp)):
                if int(tmp[k-1]) > int(tmp[k]):
                    break
            else:
                ans = max(ans,int(tmp))
    print('#{} {}'.format(tc+1,ans))