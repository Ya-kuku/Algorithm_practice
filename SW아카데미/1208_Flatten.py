for tc in range(10):
    pos = int(input())
    boxes = list(map(int,input().split()))
    for _ in range(pos):
        a = max(boxes)
        b = min(boxes)
        a -= 1
        b += 1
    print('#{} {}'.format(tc+1,max(s)))
