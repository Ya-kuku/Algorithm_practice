# import sys
# INF = 1e9
# n = int(input())
# m = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
#
# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 a[i][j] = 1
#             if a[i][k] and a[k][j]:
#                 a[i][j] = 1
#
# d = list(map(int, input().split()))
# for i in range(len(d)-1):
#     if a[d[i]-1][d[i+1]-1] != 1:
#         print("NO")
#         sys.exit()
# print("YES")

import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())  # 도시의 수
M = int(input())  # 여행에 속한 도시 수
parent = [i for i in range(N + 1)]


def find_root(target):
    if target == parent[target]:
        return parent[target]
    parent[target] = find_root(parent[target])
    return parent[target]


def union(a, b):
    a = find_root(a)
    b = find_root(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


for i in range(1, N + 1):
    arr = list(map(int, input().split()))
    for j in range(1, N + 1):
        if arr[j - 1] == 1:
            union(i, j)

destination = list(map(int, input().split()))
start = find_root(destination[0])
check = 1
for i in destination[1:]:
    if start != find_root(i):
        check = 0
        break

if check == 1:
    print("YES")
else:
    print("NO")