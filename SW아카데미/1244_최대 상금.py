def dfs(cnt):
    global ans
    if cnt == 0:
        tmp = int(''.join(nums))
        ans = max(ans,tmp)
        return

    # 스왑을 해서 바꿔야하기 때문에 이중 포문 사용
    for i in range(N):
        for j in range(i+1,N):
            nums[i], nums[j] = nums[j], nums[i]
            tmp_cur = ''.join(nums)
            if not visited.get((tmp_cur,cnt-1),0):
                visited[(tmp_cur,cnt-1)] = 1
                dfs(cnt-1)
            nums[i], nums[j] = nums[j], nums[i]

for tc in range(int(input())):
    a,b = input().split()
    ans = 0
    # 바꿀횟수
    swap = int(b)
    # 입력받은 숫자
    nums = list(a)
    # 입력받은 숫자 길이
    N = len(nums)
    # 스왑한 동일 숫자 확인
    visited= dict()
    dfs(swap)
    print('#{} {}'.format(tc+1,ans))