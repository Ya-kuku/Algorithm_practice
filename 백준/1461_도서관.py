import heapq

n, m = map(int,input().split())
arr= list(map(int,input().split()))
positive = []
negative = []

Max_dist = max(max(arr),-min(arr))

# 최대 힙을 사용하기 위해 원소를 음수값으로 지정
for i in arr:
    if i > 0:
        heapq.heappush(positive,-i)
    else:
        heapq.heappush(negative,i)

res = 0

while positive:
    # 한번에 옮길 수 있는 책 m 개에서 한개를 뽑고
    res += heapq.heappop(positive)
    # 나머지 m-1개를 뽑아주는데
    for _ in range(m-1):
        # 원소가 있을경우에만 뽑아준다
        if positive:
            heapq.heappop(positive)

while negative:
    res += heapq.heappop(negative)
    for _ in range(m-1):
        if negative:
            heapq.heappop(negative)

# 최대힙으로 구성하느라 원소값이 음수
print(-res*2 - Max_dist)