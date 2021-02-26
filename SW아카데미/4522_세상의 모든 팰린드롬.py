for tc in range(int(input())):
    words = list(input())
    ans = 'Not exist'
    for i in range(len(words)):
        if words[i] == '?':
            words[i] = words[-(i + 1)]
    if words == words[::-1]:
        ans = "Exist"
    print('#{} {}'.format(tc+1,ans))