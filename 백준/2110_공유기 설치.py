def check(distance):
    cnt = 1
    cur_home = home[0]
    for i in range(1,N):
        if distance <= home[i] - cur_home:
            cnt += 1
            cur_home = home[i]
    return cnt

def divide(count):
    st = 1
    end = home[-1] - home[0]

    while st <= end:
        mid = (st+end) // 2
        check_cnt = check(mid)
        if check_cnt < count:
            end = mid - 1
        else:
            ans = mid
            st = mid + 1
    return ans

N, C = map(int,input().split())
home = [int(input()) for _ in range(N)]
home.sort()
print(divide(C))
