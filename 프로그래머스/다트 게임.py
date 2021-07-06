def solution(dart):
    answer = 0
    tmp = ''
    tmp_ans = []
    for i in range(len(dart)):
        if dart[i].isdigit():
            tmp += dart[i]
        if dart[i].isalpha():
            if dart[i] == 'S':
                tmp_ans.append(int(tmp) ** 1)
            elif dart[i] == 'D':
                tmp_ans.append(int(tmp) ** 2)
            else:
                tmp_ans.append(int(tmp) ** 3)
            tmp = ''
        if dart[i] == '*':
            if len(tmp_ans) >= 2:
                tmp_ans[-2] *= 2
                tmp_ans[-1] *= 2
            else: tmp_ans[-1] *= 2
        if dart[i] == '#':
            # if len(tmp_ans) >= 2:
            #     tmp_ans[-2] *= -1
            #     tmp_ans[-1] *= -1
            tmp_ans[-1] *= -1
    print(tmp_ans)
    return answer

solution('1D2S#10S')