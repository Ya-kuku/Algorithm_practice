N = int(input())
nums = sorted([int(input()) for i in range(N)])
print(*nums, sep='\n')