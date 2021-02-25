# from itertools import combinations
# for tc in range(int(input())):
#     n, k = map(int,input().split())
#     arr = list(map(int,input().split()))
#
#     cnt = 0
#     for r in range(1, n + 1):
#         cm = combinations(arr, r)
#         for c in cm:
#             if sum(c) == k:
#                 cnt += 1
#
#     print('#{} {}'.format(tc+1,cnt))
#
#
n, s = map(int, input().split())
a = list(map(int, input().split()))
ans = 0

def solve(index, sums):
    global ans
    if index >= n:
        if sums == s:
            ans += 1
        return
    solve(index+1, sums+a[index])
    solve(index+1, sums)

solve(0, 0)
print(ans if s else ans-1)


