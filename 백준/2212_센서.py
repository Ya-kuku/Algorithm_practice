import sys
n = int(input())
k = int(input())
sensor = sorted(list(map(int,input().split())))

if k >= n:
    print(0)
    sys.exit()

dist = []
for i in range(1,n):
    dist.append(sensor[i] - sensor[i-1])

dist.sort(reverse=True)
# 제일 긴 구간의 차이값을 뺄때 한개 빼면 2개의 구획, 2개 빼면 3개의 구획이므로 k개의 기지국에서 -1한 값까지가 범위가 된다
for _ in range(k-1):
    dist.pop(0)

print(sum(dist))
