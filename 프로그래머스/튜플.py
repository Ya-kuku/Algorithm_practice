def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split('},{')
    s.sort(key=len)
    for i in s:
        temp = i.split(',')
        for j in temp:
            if int(j) not in answer:
                answer.append(int(j))
    return answer
print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))


import re
from collections import Counter

def solution1(s):
    # 정규표현식 풀이
    # \d  숫자 0~9와 같음
    s = Counter(re.findall('\d+',s))
    return list(map(int,[k for k,v in sorted(s.items(), key=lambda x:x[1])]))
solution1("{{2},{2,1},{2,1,3},{2,1,3,4}}")