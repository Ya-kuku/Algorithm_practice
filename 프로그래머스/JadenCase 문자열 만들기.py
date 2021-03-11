def solution(s):
    s = s.lower()
    _s = s.split(' ')
    answer = ''
    for i in _s:
        for j in range(len(i)):
            if i[j] == ' ':
                answer += ' '
            else:
                answer += i[:j] + i[j].upper() + i[1:]
                break
        answer += ' '
    return answer[:-1]

print(solution("3people   unFollowed me"))
# a = "3people   unFollowed me"
# print(a.split(' '))
print(len(' '))