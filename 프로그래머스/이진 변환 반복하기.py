def solution(s):
    # 변환 수, 0의 수
    answer = [0,0]
    while s != '1':
        answer[1] += s.count('0')
        temp = s.replace('0','')
        s = bin(len(temp))[2:]
        answer[0] += 1

    return answer

print(solution('1111111'))