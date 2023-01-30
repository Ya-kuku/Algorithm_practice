def solution(my_str, n):
    answer = []
    str_len = len(my_str)
    cnt = 0
    while 1:
        if cnt * n >= str_len:
            break
        answer.append(my_str[cnt*n:n*(cnt+1)])
        cnt += 1
    print(answer)
    return answer

solution("abc1Addfggg4556b",6)
