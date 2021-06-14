def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n

    while left <= right:
        mid = (left + right) // 2
        pos_num = 0

        for time in times:
            pos_num += mid // time

            if pos_num >= n:
                break
        # 검사 가능한 사람의 수가 더 많으면
        if pos_num >= n:
            answer = mid
            right = mid - 1

        # 검사 가능한 사람의 수가 n보다 작으면
        else:
            left = mid + 1

    return answer

solution()