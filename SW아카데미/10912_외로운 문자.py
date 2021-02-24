for tc in range(int(input())):
    words = list(input())
    # words.sort()
    words_set = set(words)
    res = []
    for word in words_set:
        tmp = words.count(word)
        if tmp % 2:
            res.append(word)
    print('#{}'.format(tc+1),end=' ')
    res.sort()
    if res:
        print(*res,sep='')
    else:
        print('Good')
    cur = 0
