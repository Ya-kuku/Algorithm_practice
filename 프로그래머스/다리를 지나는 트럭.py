def solution(bridge_length, weight, truck_weights):
    q = [0] * bridge_length
    answer = 0
    while q:
        answer += 1
        q.pop(0)
        if truck_weights:
            if sum(q)+truck_weights[0]<=weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return answer

a = 2
b = 10
c = [7,4,5,6]
solution(a,b,c)