N = int(input())
point = []
for _ in range(N):
    x,y = (map(int,input().split()))
    point.append((x,y))
point.sort(key=lambda x:(x[0],x[1]))
for i in range(N):
    print(point[i][0],point[i][1])