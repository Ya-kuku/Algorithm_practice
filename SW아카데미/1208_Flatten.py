for tc in range(10):
    pos = int(input())
    boxes = list(map(int,input().split()))
    for _ in range(pos):
        boxes.sort()
        boxes[0] += 1
        boxes[-1] -= 1
    print('#{} {}'.format(tc+1,max(boxes)-min(boxes)))
