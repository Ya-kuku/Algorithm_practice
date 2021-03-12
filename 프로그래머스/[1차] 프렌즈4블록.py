dirs = [(0,1),(1,1),(1,0)]
def check(r,c,board):
    shape = board[r][c]
    tmp = [(r,c)]
    for i in range(3):
        nr = r + dirs[i][0]
        nc = c + dirs[i][1]
        if board[nr][nc] == shape:
            tmp.append((nr,nc))

    if len(tmp) == 4:
        return tmp
    else:
        return False

def move(m,n,save_point,board):
    for point in save_point:
        board[point[0]][point[1]] = 0

    # 행만큼 반복해주고
    # 한개요소씩 계속 위치 바꿔주면서 순회한다
    for _ in range(m):
        for j in range(n):
            for i in range(m - 1):
                if board[i][j] != 0 and board[i + 1][j] == 0:
                    board[i][j], board[i + 1][j] = 0, board[i][j]

    return


def solution(m, n, board):
    # m 세로 n 가로
    answer = 0
    board = [list(i) for i in board]
    while 1:
        save_point = []
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != 0:
                    tmp = check(i,j,board)
                    if tmp:
                        save_point.extend(check(i,j,board))
        save_point = list(set(save_point))
        if not save_point:
            break
        else:
            move(m,n,save_point,board)

    for i in board:
        answer += i.count(0)
    return answer
a= 4
b = 5
c = [[1,1,3,],
     [5,0,0,0],
     [0,0,0,12]]
# c = list(map(list,zip(*c[::-1])))
# print(list(map(list,zip(*c))))

