for tc in range(int(input())):
    N,Q = map(int,input().split())
    boxes = [0] * (N)
    for i in range(1,Q+1):
        a,b = map(int,input().split())
        for j in range(a-1,b):
            boxes[j] = i
    print('#{}'.format((tc+1)),end=' ')
    print(*boxes)