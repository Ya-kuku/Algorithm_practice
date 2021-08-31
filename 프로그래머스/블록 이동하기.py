from collections import deque
def bfs(cur,arr):
    position = []
    (x1,y1),(x2,y2) = cur
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    # 평행이동
    for dir in dirs:
        if arr[x1+dir[0]][y1+dir[1]] == 0 and arr[x2+dir[0]][y2+dir[1]] == 0:
            position.append({(x1+dir[0],y1+dir[1]),(x2+dir[0],y2+dir[1])})

    # 로봇의 위치가 세로인 경우
    if y1 == y2:
        for i in [-1,1]:
            if arr[x1][y1+i] == 0 and arr[x2][y2+i] == 0:
                position.append({(x1,y1),(x1,y1+i)})
                position.append({(x2, y2), (x2, y2 + i)})

    elif x1 == x2:
        for i in [-1,1]:
            if arr[x1+i][y1] == 0 and arr[x2+i][y2] == 0:
                position.append({(x1,y1),(x1+i,y1)})
                position.append({(x2, y2), (x2+i, y2)})

    return position
def solution(board):
    n = len(board)
    new_board = [[-1] * (n+2) for _ in range(n+2)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            new_board[i][j] = board[i-1][j-1]

    st = {(1,1),(1,2)}
    q = deque()
    q.append((st,0))
    visited = [st]
    while q:
        cur, dist = q.popleft()
        if (n,n) in cur: return dist
        # next_position = bfs(cur,new_board)
        # print(next_position)
        for pos in bfs(cur,new_board):
            if pos not in visited:
                visited.append(pos)
                q.append((pos,dist+1))
print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
