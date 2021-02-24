for tc in range(int(input())):
    arr = list(input().split())
    N = int(arr[0])
    B, O, order = [], [], []
    for i in range(1,len(arr),2):
        order.append(arr[i])
        if arr[i] == 'B':
            B.append(int(arr[i+1]))
        if arr[i] == 'O':
            O.append(int(arr[i+1]))
    B_cur = O_cur = 1
    res = 0
    while order:
        res += 1
        now_bot = order[0]
        if len(B):
            if B_cur == B[0]:
                if now_bot == 'B':
                    B.pop(0)
                    order.pop(0)
            elif B_cur > B[0]: B_cur -= 1
            else: B_cur += 1

        if len(O):
            if O_cur == O[0]:
                if now_bot == 'O':
                    O.pop(0)
                    order.pop(0)
            elif O_cur > O[0]: O_cur -= 1
            else: O_cur += 1

    print('#{} {}'.format(tc+1, res))
