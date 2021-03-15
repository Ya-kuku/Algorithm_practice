alpa = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def solution(msg):
    answer = []
    cur_st = 0
    while cur_st < len(msg):
        # 현재 위치
        tmp_p = 0
        while 1:
            print(alpa)
            word = ''.join(msg[cur_st:len(msg)-tmp_p])
            if word in alpa:
                answer.append(alpa.index(word)+1)
                alpa.append(''.join(msg[cur_st:len(msg)-tmp_p+1]))
                cur_st = len(msg)-tmp_p
                break
            else:
                tmp_p += 1
    print(''.join(alpa[2:4]))
    print(answer)
    return answer

solution('KAKAO')