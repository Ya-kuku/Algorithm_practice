import heapq
N = int(input())
cards = []

for _ in range(N):
    heapq.heappush(cards,int(input()))

res = 0
while len(cards) != 1:
    one = heapq.heappop(cards)
    two = heapq.heappop(cards)
    tmp = one + two
    res += tmp
    heapq.heappush(cards,tmp)
print(res)