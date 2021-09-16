def dfs(idx,total):
    global ans

    if idx == len(op):
        ans = max(ans,int(total))
        return

    first = str(eval(total + op[idx] + nums[idx + 1]))
    dfs(idx+1, first)

    if idx +1 < len(op):
        second = str(eval(nums[idx + 1] + op[idx + 1] + nums[idx + 2]))
        second = str(eval(total + op[idx] + second))
        dfs(idx+2, second)

n = int(input())
formula = input()
ans = -1e9
nums = []
op = []
for fo in formula:
    if fo.isdigit():
        nums.append(fo)
    else:
        op.append(fo)

dfs(0,nums[0])
print(ans)