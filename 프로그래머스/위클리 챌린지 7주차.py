def solution(enter, leave):
    n = len(enter)
    answer = [0] * (n+1)
    room = []
    idx_enter = 0
    idx_leave = 0
    tmp = []
    while idx_leave < n:
        if leave[idx_leave] in room:
            room.remove(leave[idx_leave])
            idx_leave += 1
            continue

        if enter[idx_enter] not in room:
            for a in room:
                answer[a] += 1
            answer[enter[idx_enter]] = len(set(room))
            room.append(enter[idx_enter])
            idx_enter += 1
    print(answer)
    return answer

solution([1,4,2,3],[2,1,3,4])