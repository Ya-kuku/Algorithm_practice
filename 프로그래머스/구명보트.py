from collections import deque
def solution(people, limit):
    people.sort()
    answer = 0
    q = deque(people)
    while q:
        if len(q) >= 2:
            if q[0] + q[-1] <= limit:
                q.popleft()
                q.pop()
                answer += 1
            else:
                q.pop()
                answer += 1
        else:
            q.pop()
            answer += 1
    return answer

# 속도가 더 빠름
# def solution(people, limit):
#     answer = len(people)
#     p = sorted(people,reverse = True)
#     s,e = 0, len(p)-1
#     while s < e :
#         if p[s]+p[e] <= limit :
#             e-=1
#             answer-=1
#         s+=1
#     return answer
print(solution([70,50,80,50],100))