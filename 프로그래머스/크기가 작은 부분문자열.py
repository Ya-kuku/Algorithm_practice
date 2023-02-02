def solution(t, p):
    answer = 0
    n = len(p)
    for i in range(len(t)-n+1):
        tmp = t[i:i+n]
        print(tmp)
        if len(tmp) < n: break
        if int(tmp) <= int(p):
            answer += 1
    return answer

#print(solution("3141592", "271"))
#print(solution("500220839878", "7"))
print(solution("10203", "15"))