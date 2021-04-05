# n 원판개수, m 원판안의 숫자 개수, t 몇번돌릴지
n, m, t = map(int,input().split())
circle = [list(map(int,input().split())) for _ in range(n)]
circle = [[]] + circle
cmds = []
for _ in range(t):
    cmds.append(list(map(int,input().split())))

# cmd[1] = 0 시계방향 1 반시계 방향
for cmd in cmds:
    # 배수, 방향, 돌릴 횟수
    multi, di, cnt = cmd
    # 원판 회전
    for _ in range(cnt):
        for i in range(1,n+1):
            if i % multi == 0:
                if di == 0:
                    circle[i] = [circle[i].pop()] + circle[i]
                else:
                    circle[i] = circle[i] + [circle[i].pop(0)]

    # 인접 숫자 초기화
    flag = False
    tmp = [[0] * (m) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(m):
            if circle[i][j] == 'x':
                continue
            else:
                if circle[i][j] == circle[i][(j+1) % m]:
                    tmp[i][j] = 'x'
                    tmp[i][(j+1) % m] = 'x'
                    flag = True
                if circle[i][j] == circle[i][j-1]:
                    tmp[i][j], tmp[i][j - 1] = 'x', 'x'
                    flag = True
                if i != 1 and circle[i][j] == circle[i - 1][j]:
                    tmp[i][j], tmp[i - 1][j] = 'x', 'x'
                    flag = True
                if i != n and circle[i][j] == circle[i+1][j]:
                    tmp[i][j],tmp[i+1][j] = 'x','x'
                    flag = True
    for i in range(1,n+1):
        for j in range(m):
            if tmp[i][j] =='x': continue
            tmp[i][j] = circle[i][j]
    circle = tmp

    if not flag:
        tmp_sum = 0
        tmp_cnt = 0
        for i in range(1,n+1):
            for j in range(m):
                if circle[i][j] != 'x':
                    tmp_sum += circle[i][j]
                    tmp_cnt += 1
        if tmp_cnt:
            num = tmp_sum / tmp_cnt
            for i in range(1,n+1):
                for j in range(m):
                    if circle[i][j] != 'x':
                        if circle[i][j] > num:
                            circle[i][j] -= 1
                        elif circle[i][j] < num:
                            circle[i][j] += 1
SUM = 0
for i in range(1,n+1):
    for j in range(m):
        if circle[i][j] != 'x':
            SUM += circle[i][j]

print(SUM)