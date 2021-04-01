r,c,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(3)]
row, col = 3,3
cnt = 0

def cal_row(arr):
    tmp_arr = []
    for nums in arr:
        Count_nums = dict()
        num = list(set(nums))
        for i in num:
            Count_nums[i] = nums.count(i)
        Count_nums = sorted(Count_nums.items(),key=lambda data: (data[1],data[0]))
        tmp = []
        for Count in Count_nums:
            if Count[0] == 0: continue
            tmp.append(Count[0])
            tmp.append(Count[1])
        tmp_arr.append(tmp)
    col = max(len(length) for length in tmp_arr)
    row = len(tmp_arr)

    new_arr = [[0] * col for _ in range(row)]
    for i in range(len(tmp_arr)):
        for j in range(len(tmp_arr[i])):
            new_arr[i][j] = tmp_arr[i][j]

    return new_arr

def cal_col(arr):
    b = [list(p) for p in zip(*arr)]
    tmp_arr = []
    for nums in b:
        Count_nums = dict()
        num = list(set(nums))
        for i in num:
            Count_nums[i] = nums.count(i)
        Count_nums = sorted(Count_nums.items(), key=lambda data: (data[1], data[0]))
        tmp = []
        for Count in Count_nums:
            if Count[0] == 0: continue
            tmp.append(Count[0])
            tmp.append(Count[1])
        tmp_arr.append(tmp)
    col = max(len(length) for length in tmp_arr)
    row = len(tmp_arr)

    new_arr = [[0] * col for _ in range(row)]
    for i in range(len(tmp_arr)):
        for j in range(len(tmp_arr[i])):
            new_arr[i][j] = tmp_arr[i][j]

    rotate_arr = [list(p) for p in zip(*new_arr)]
    return rotate_arr


while cnt <= 100:
    if 0<= r-1 < row and 0 <= c-1 < col:
        if board[r-1][c-1] == k:
            break

    if row >= col:
        board = cal_row(board)
        row = len(board)
        col = len(board[0])
    else:
        board = cal_col(board)
        row = len(board)
        col = len(board[0])

    cnt +=1


if cnt > 100:
    print(-1)
else:
    print(cnt)