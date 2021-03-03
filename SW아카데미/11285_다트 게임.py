for tc in range(int(input())):
    N = int(input())
    arr = [tuple(map(int,input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        a,b = arr[i][0], arr[i][1]
        rad = float((a ** 2 + b ** 2)**(0.5))
        if rad <= 20:
            ans += 10
        elif 20 < rad <= 40:
            ans += 9
        elif 40 < rad <= 60:
            ans += 8
        elif 60 < rad <= 80:
            ans += 7
        elif 80 < rad <= 100:
            ans += 6
        elif 100 < rad <= 120:
            ans += 5
        elif 120 < rad <= 140:
            ans += 4
        elif 140 < rad <= 160:
            ans += 3
        elif 160 < rad <= 180:
            ans += 2
        elif 180 < rad <= 200:
            ans += 1
    print('#{} {}'.format(tc+1,ans))