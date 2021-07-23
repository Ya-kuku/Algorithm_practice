def solution(n, k, cmd):
    exists = [True for _ in range(n)]
    up = [-1] + [i for i in range(n-1)]
    down = [i for i in range(1,n)] + [-1]
    deleted = []

    for c in cmd:
        op = c[0]

        # 위로 / 중간 인덱스가 비어있을 수 있으니 순차적으로 찾아줘야 함
        if op == 'U':
            # 위치 옮기는 숫자 한자리 수가 아닐 수 있음
            val = int(c.split()[1])
            for _ in range(val):
                k = up[k]
        # 아래로
        elif op == 'D':
            val = int(c.split()[1])
            for _ in range(val):
                k = down[k]

        elif op == 'C':
            if up[k] != -1:
                down[up[k]] = down[k]

            if down[k] != -1:
                up[down[k]] = up[k]
            exists[k] = False
            deleted.append(k)
            k = down[k] if down[k] != -1 else up[k]

        else:
            d = deleted.pop()
            if up[d] != -1:
                down[up[d]] = d
            if down[d] != -1:
                up[down[d]] = d
            exists[d] = True

    return ''.join(['O' if x else 'X' for x in exists])