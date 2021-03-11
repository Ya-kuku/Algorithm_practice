def solution(n):
    answer = 1
    temp = n //2 + 2
    for i in range(1,temp):
        ans = 0
        for j in range(i,temp):
            ans += j
            if ans == n:
                answer += 1
            elif ans > n:
                break
    return answer