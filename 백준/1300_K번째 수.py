def solve(data):
    if len(data) <= 1:
        return data
    mid = len(data)//2
    left = solve(data[:mid])
    right = solve(data[mid:])

    i = j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]

    return res
N = int(input())
k = int(input())
nums = []
array = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        nums.append((i+1)*(j+1))

print(solve(nums)[k+1])