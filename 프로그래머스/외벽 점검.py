from itertools import permutations

def solution(n, weak, dist):
    INF = 987654321
    answer = INF
    weak_point = weak + [ w + n for w in weak ]
    L = len(weak)
    # 시작점
    for (idx, start) in enumerate(weak):
        # 가능한 모든 케이스의 순열
        for p in permutations(dist):
            count = 1
            pos = start
            for d in p:
                pos += d
                if pos >= weak_point[idx + L - 1]:
                    answer = min(answer, count)
                else:
                    pos = [w for w in weak_point if w > pos][0]
                    count += 1
    return -1 if answer == INF else answer

solution(12,[1,5,6,10],[1,2,3,4])