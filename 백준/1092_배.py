n = int(input())
crane = list(map(int,input().split()))
m = int(input())
boxes = list(map(int,input().split()))
if max(crane) < max(boxes):
    print(-1)
else:
    crane.sort(reverse=True)
    boxes.sort(reverse=True)
    position = [0] * n
    checked = [False] * m
    cnt = 0
    res = 0
    while 1:
        if cnt == len(boxes):
            break
        for i in range(n):
            # position에서 각 크레인이 다음에 옮겨야할 박스의 인덱스를 저장
            while position[i] < len(boxes):
                # 0번 크레인이 0번 박스를 옮겼을 경우, position 1번에 1번 박스를 옮겨야 한다고 인덱스 저장해줌
                if not checked[position[i]] and crane[i] >= boxes[position[i]]:
                    # 옮겨진 박스의 인덱스는 값을 바꿔줌
                    checked[position[i]] = True
                    position[i] += 1
                    cnt += 1
                    break
                position[i] += 1
        res += 1
    print(res)
