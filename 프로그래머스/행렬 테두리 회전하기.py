def solution(rows, columns, queries):
    answer = []
    arr = [[0] * columns for _ in range(rows)]
    st = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = st
            st += 1

    # 시계방향으로만 회전
    for query in queries:
        x1,y1,x2,y2 = query
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        stack = []

        for i in range(y1,y2):
            stack.append(arr[x1][i])

        for i in range(x1,x2):
            stack.append(arr[i][y2])

        for i in range(y2,y1,-1):
            stack.append(arr[x2][i])

        for i in range(x2,x1,-1):
            stack.append(arr[i][y1])

        answer.append(min(stack))
        stack = [stack[-1]] + stack[:-1]

        st = 0
        while st < len(stack):
            for i in range(y1,y2):
                arr[x1][i] = stack[st]
                st += 1

            for i in range(x1,x2):
                arr[i][y2] = stack[st]
                st += 1

            for i in range(y2,y1,-1):
                arr[x2][i] = stack[st]
                st += 1

            for i in range(x2,x1,-1):
                arr[i][y1] = stack[st]
                st += 1
    print(answer)
    return answer

solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])