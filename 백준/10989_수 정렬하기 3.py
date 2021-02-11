# N = int(input())
# ans = []
# for _ in range(N):
#     ans.append(int(input()))
# ans.sort()
# print(*ans,sep='\n')

import sys
# 파이썬에서 데이터의 개수가 많을 때는 stdin.readline()을 사용해줘야함 기본 input()보다 속도가 빠름
N = int(sys.stdin.readline())
array = [0] * 10001
# 계수정렬 = 카운팅 정렬
# 파이썬의 정렬이나 다른 정렬법은 nlogn의 시간복잡도가 나오는데
# 주어진 범위가 한정적일 때, 여기서는 정수의 범위가 0~10000까지
# 카운팅 정렬을 사용하면 시간복잡도 O(n)
for i in range(N):
    data = int(sys.stdin.readline())
    array[data] += 1

for i in range(10001):
    if array[i]:
        for j in range(array[i]):
            print(i)