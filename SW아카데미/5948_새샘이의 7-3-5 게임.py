# for tc in range(int(input())):
#     nums = list(map(int,input().split()))
#     tmp = []
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             for k in range(j+1,len(nums)):
#                 a = nums[i] + nums[j] + nums[k]
#                 tmp.append(a)
#
#     tmp = list(set(tmp))
#     tmp.sort()
#     tmp = tmp[::-1]
#     print('#{} {}'.format(tc+1,tmp[4]))

from itertools import combinations
for tc in range(int(input())):
    nums = list(map(int,input().split()))
    res = []
    tmp = list(combinations(nums,3))
    for i in tmp:
        res.append(sum(i))
    ans = list(set(res))
    ans.sort()
    print('#{} {}'.format(tc+1,ans[-5]))

