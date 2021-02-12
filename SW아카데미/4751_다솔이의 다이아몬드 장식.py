dr = [-2,-1,0,1,2,1,0,-1]
dc = [0,1,2,1,0,-1,-2,-1]
for tc in range(int(input())):
    word = input()
    arr = [['.'] * (4 * len(word) + 1) for _ in range(5)]

    for i in range(len(word)):
        r = 2
        c = 2 + (4*i)
        arr[r][c] = word[i]

        for j in range(8):
            nr = r + dr[j]
            nc = c + dc[j]
            arr[nr][nc] = '#'

    for i in range(5):
        print(*arr[i][:], sep='')

