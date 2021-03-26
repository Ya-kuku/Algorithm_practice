n, s = map(int,input().split())
arr = list(map(int,input().split()))

ans = 1e9
st = 0
end = 0
Sum_arr = 0
if Sum_arr == s:
    ans = 1

while 1:
    if Sum_arr >= s:
        ans = min(ans,end-st)
        Sum_arr -= arr[st]
        st += 1

    elif end == n:
        break
    else:
        Sum_arr += arr[end]
        end += 1


if ans == 1e9:
    print(0)
else:
    print(ans)