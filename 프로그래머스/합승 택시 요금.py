def solution(n, s, a, b, fares):
    arr = [[1e9] * (n+1) for _ in range(n+1)]
    for fare in fares:
        x,y,cost = fare
        arr[x][y] = cost
        arr[y][x] = cost

    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                if i == j: arr[i][j] = 0; continue
                if arr[i][k] + arr[k][j] < arr[i][j]:
                    arr[i][j] = arr[i][k] + arr[k][j]

    answer = arr[s][a] + arr[s][b]

    for i in range(1,n+1):
        dist = 0
        if i == s: continue
        dist += arr[s][i] + arr[i][a] + arr[i][b]
        answer = min(dist,answer)
    return answer

solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
