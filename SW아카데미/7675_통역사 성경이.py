t = int(input())

for tc in range(1,t+1):
    n = int(input())
    s = list(map(str,input().split()))
    res = []
    cnt = 0
    for word in s:
        if word[-1] =='.' or word[-1] =='?' or word[-1] =='!':
            if word[0].isupper():
                cnt += 1 if all([c.islower() for c in word[1:len(word)-1]]) else 0
            res.append(cnt)
            cnt = 0
        else:
            if word[0].isupper():
                cnt += 1 if all([c.islower() for c in word[1:len(word)]]) else 0
    print('#{}'.format(tc),end=" ")
    print(*res)   