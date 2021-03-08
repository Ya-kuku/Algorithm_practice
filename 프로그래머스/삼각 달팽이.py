def solution(n):
    answer = [[0] * n for _ in range(n)]
    dr = [(1,0),(0,1),(-1,-1)]
    i = 0
    j= 0
    cnt = 1
    dirs = 0
    if n % 2:
        tmp = int((n*n)//2) + int(n//2) + 2
    else:
        tmp = int((n * n) // 2) + int(n // 2) + 1
    while cnt < tmp:
        dirs = dirs % 3
        while 1:
            if 0 <= i < n and 0 <= j < n and not answer[i][j]:
                answer[i][j] = cnt
                cnt += 1
                i += dr[dirs % 3][0]
                j += dr[dirs % 3][1]
            else:
                if dirs == 0:
                    dirs +=1
                    i -= 1
                    i += dr[dirs % 3][0]
                    j += dr[dirs % 3][1]
                elif dirs == 1:
                    dirs += 1
                    j -= 1
                    i += dr[dirs % 3][0]
                    j += dr[dirs % 3][1]
                else:
                    dirs += 1
                    i+=1
                    j+=1
                    i += dr[dirs % 3][0]
                    j += dr[dirs % 3][1]
                break
    res = []
    for i in range(n):
        for j in range(n):
            if answer[i][j]:
                res.append(answer[i][j])
    return res


a = [4,5,6]
for x in a:
    print(solution(x))