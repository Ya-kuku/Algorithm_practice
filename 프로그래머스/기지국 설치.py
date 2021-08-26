# import math
# def solution(n, stations, w):
#     ans = 0
#     distance = []
#
#     for i in range(1, len(stations)):
#         distance.append((stations[i]-w-1) - (stations[i-1]+w))
#
#     distance.append(stations[0]-w-1)
#     distance.append(n - (stations[-1]+ w))
#
#     for i in distance:
#         if i <= 0: continue
#         ans += math.ceil(i / ((w*2) + 1))
#     return ans
# solution(11,[4,11],1)

import math
def solution(n, stations, w):
    answer = 0
    distance = []
    left = 1
    for station in stations:
        right = station - w - 1
        if left > right: pass # 왼쪽길이 넘어감
        else: distance.append([left,right])
        # 오른쪽 전파 닿는 거리 + 1 = 다음 스테이션에서 전파가 닿지 않는 왼쪽 위치
        left = station + w + 1

    if left <= n: distance.append([left,n])
    for dist in distance:
        answer += math.ceil((dist[1] - dist[0] + 1) / (w*2 + 1))

    return answer
solution(11,[4,11],1)
