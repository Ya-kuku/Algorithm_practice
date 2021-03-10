def solution(arr):
    answer = [0] * 2
    length = len(arr)

    def check(r, c, n, arr):
        cur = arr[r][c]
        # 잘라낸 사각형에서 전부 같을 때는 사각형 내부의 숫자위치에 ans +=1을 해준다
        # 동일숫자로 이루어진 사각형은 더 이상 자르지 않고 해당 값 하나만 추가하게 됨
        # 제일 작은 단위로 쪼개진 사각형은 1x1이 4개 나오더라도 각각 하나씩 값이 추가됨
        for i in range(r, r + n):
            for j in range(c, c + n):
                if arr[i][j] != cur:
                    n = n // 2
                    # 왼쪽 위
                    check(r, c, n, arr)
                    # 오른쪽 위
                    check(r, c + n, n, arr)
                    # 왼쪽 아래
                    check(r + n, c, n, arr)
                    # 오른쪽 아래
                    check(r + n, c + n, n, arr)
                    return

        answer[cur] += 1

    check(0, 0, length, arr)
    return answer