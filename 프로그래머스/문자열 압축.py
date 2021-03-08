def solution(s):
    answer = ''
    Min_value = 1e9
    n = len(s)
    if n == 1:
        Min_value = 1
        return Min_value
    for i in range(1,n //2 + 1):
        cnt = 1
        tmp_str = s[:i]
        for k in range(i,n,i):
            if s[k:k+i] == tmp_str:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ''
                answer += str(cnt) + tmp_str
                tmp_str = s[k:k+i]
                cnt = 1
        if cnt == 1:
            cnt = ''
        answer += str(cnt) + tmp_str
        Min_value = min(Min_value, len(answer))
        answer = ''

    return Min_value

a = "aabbaccc"
solution(a)
