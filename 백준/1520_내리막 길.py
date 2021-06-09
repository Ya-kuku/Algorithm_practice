import heapq
import sys
input = sys.stdin.readline
M, N = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(M)]
dirs = [(0,1),(1,0),(-1,0),(0,-1)]

def bfs():
    heap = []
    heap.append((-lst[0][0],0,0))

    dp = [[0] * N for _ in range(M)]
    dp[0][0] = 1

    while heap:
        cnt, r, c = heapq.heappop(heap)

        for dir in dirs:
            nr = r + dir[0]
            nc = c + dir[1]

            if 0 <= nr < M and 0 <= nc < N:
                if lst[nr][nc] < lst[r][c]:
                    if not dp[nr][nc]:
                        heapq.heappush(heap,(-lst[nr][nc],nr,nc))
                    dp[nr][nc] += dp[r][c]
                    for d in dp:
                        print(d)
                    print()
    return dp[M-1][N-1]

print(bfs())
