def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True


def backtrack(idx):
    global res
    if idx == N:
        res += 1
        return
    for i in range(N):
        row[idx] = i
        if check(idx):
            backtrack(idx + 1)

for tc in range(int(input())):
    N = int(input())
    row = [0] * N
    res = 0
    backtrack(0)
    print('#{} {}'.format(tc+1,res))


def backtracking(n, level):
    global result
    if level == n:
        result += 1
        return

    for x in range(n):
        # col: 같은 열, diag1 : '\' 방향, diag2 : '/' 방향
        if x in col or (x + level) in diag1 or (x - level) in diag2:
            continue

        col.append(x)
        diag1.append(x + level)
        diag2.append(x - level)
        # print(col, diag1, diag2)

        # 재귀로 다음 열,대각선 검사하면서 추가
        backtracking(n, level + 1)

        # 이전단계로 돌아가기
        col.remove(x)
        diag1.remove(x + level)
        diag2.remove(x - level)


for tc in range(1, 1 + int(input())):
    N = int(input())
    col, diag1, diag2 = [], [], []
    result = 0
    backtracking(N, 0)

    print('#{} {}'.format(tc, result))