import sys
A, B = map(int,input().split())
N, M = map(int,input().split())
arr = [[0] * A for _ in range(B)]
directions = {'E':(0,1), 'S':(1,0), 'W':(0,-1), 'N':(-1,0)}
direct = 'ESWN'
def move(cmds):
    x,y = 0,0
    cur_dir = ''
    for i in range(B):
        for j in range(A):
            if arr[i][j] and arr[i][j][0] == int(cmds[0]):
                x,y = i, j
                cur_dir = arr[i][j][1]
                break
    cmd = cmds[1]
    repeat = int(cmds[2])
    if cmd == 'L':
        tmp = direct.index(cur_dir) - repeat
        cur_dir = direct[tmp%4]
        arr[x][y] = [int(cmds[0]),cur_dir]
    elif cmd == 'R':
        tmp = direct.index(cur_dir) + repeat
        cur_dir = direct[tmp % 4]
        arr[x][y] = [int(cmds[0]), cur_dir]
    else:
        while repeat > 0:
            nx = x + directions[cur_dir][0]
            ny = y + directions[cur_dir][1]
            if 0 <= nx < B and 0 <= ny < A:
                if not arr[nx][ny]:
                    arr[x][y] = 0
                    arr[nx][ny] = [int(cmds[0]),cur_dir]
                    x = nx
                    y = ny
                    repeat -= 1
                else:
                    robo_idx = arr[nx][ny][0]
                    print('Robot {} crashes into robot {}'.format(cmds[0],robo_idx))
                    sys.exit()
            else:
                print('Robot {} crashes into the wall'.format(cmds[0]))
                sys.exit()

for i in range(N):
    robo = list(input().split())
    arr[B-int(robo[1])][int(robo[0])-1] = [i+1,robo[2]]
for i in range(M):
    # print(arr)
    cmds = list(input().split())
    move(cmds)
print('OK')

