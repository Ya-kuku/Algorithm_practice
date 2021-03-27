n = int(input())
nums = []
for _ in range(n):
    nums.append(list(map(int,input().split())))

nums.sort(key=lambda data : (data[1],data[0]))
for i in nums:
    print(*i)