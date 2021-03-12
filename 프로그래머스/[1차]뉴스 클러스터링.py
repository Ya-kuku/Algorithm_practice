from collections import defaultdict
def solution(str1, str2):
    answer = 0
    str1 = str1.upper()
    str2 = str2.upper()
    str1_temp = defaultdict(int)
    str2_temp = defaultdict(int)
    str_set = defaultdict(int)
    for i in range(len(str1)-1):
        a, b = str1[i], str1[i+1]
        if a.isalpha() and b.isalpha():
            str1_temp[a+b] += 1
            str_set[a+b] += 1
    # str1_temp = sorted(str1_temp.items())
    for i in range(len(str2)-1):
        a, b = str2[i], str2[i+1]
        if a.isalpha() and b.isalpha():
            str2_temp[a+b] += 1
            str_set[a + b] += 1
    # str2_temp = sorted(str2_temp.items())
    # str_set = sorted(str_set.items())
    inter = 0
    union = 0
    if str1_temp == str2_temp:
        answer = 1
    else:
        for word in str_set:
            if word in str1_temp and word in str2_temp:
                inter += min(str1_temp[word],str2_temp[word])
                union += max(str1_temp[word],str2_temp[word])
            elif word in str1_temp:
                union += str1_temp[word]
            elif word in str2_temp:
                union += str2_temp[word]
        answer = inter / union
    return int(answer * 65536)

a =  "AAbbaa_AA"
b = " BBB"
# a = 'france'
# b = 'french'
print(solution(a,b))