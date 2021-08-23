from collections import deque
dr = [0,0,1,-1]
dc = [1,-1,0,0]
# 블럭 찾기
def bfs(arr,r,c,flag):
    figure = []
    q = deque()
    q.append((r,c))
    figure.append([r,c])

    while q:
        x,y = q.popleft()
        arr[x][y] = -1
        for i in range(4):
            dx = x + dr[i]
            dy = y + dc[i]
            if 0 <= dx < len(arr) and 0 <= dy < len(arr) and arr[dx][dy] == flag:
                arr[dx][dy] = -1
                q.append((dx,dy))
                figure.append([dx,dy])

    # 평행이동
    X = min([x[0] for x in figure])
    Y = min([x[1] for x in figure])
    figure = [(s[0] - X, s[1] - Y) for s in figure]

    return sorted(figure)

def rotate(arr):
    n = len(arr)
    rotate_figures = [arr,[],[],[]]
    for ar in arr:
        x,y = ar
        rotate_figures[1].append([n - y, x])
        rotate_figures[2].append([n - x, n - y])
        rotate_figures[3].append([y, n - x])

    # 회전시킨 배열 다시 평행이동
    for i in range(1,4):
        X = min([x[0] for x in rotate_figures[i]])
        Y = min([x[1] for x in rotate_figures[i]])
        rotate_figures[i] = sorted([(s[0] - X, s[1] - Y) for s in rotate_figures[i]])

    return min(sorted(rotate_figures))

def solution(game_board, table):
    answer = 0
    # shapes = 도형의 모양
    # spaces = 빈칸의 모양
    shapes = []; spaces = []
    n = len(table)
    for i in range(n):
        for j in range(n):
            #table = 1
            if table[i][j] == 1:
                figure_table = bfs(table,i,j,1)
                figure_table_rotate = rotate(figure_table)
                shapes.append(figure_table_rotate)
            # game_board = 0
            if game_board[i][j] == 0:
                figure_game_board = bfs(game_board, i, j, 0)
                figure_game_board_rotate = rotate(figure_game_board)
                spaces.append(figure_game_board_rotate)

    # 빈칸의 모형이 존재하는 도형의 모양과 같은 경우에
    for space in spaces:
        for shape in shapes:
            print(shape,'shape')
            if space == shape:  # 같은 모양이 있다면
                answer += len(shape)  # 블록의 개수만큼 더한다
                shapes.remove(shape)  # 사용된 블록은 제거
                break
    print(answer)
    return answer
solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
         [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])