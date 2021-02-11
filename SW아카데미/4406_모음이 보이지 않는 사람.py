vowel = ['a','e','i','o','u']
for tc in range(1,int(input())+1):
    word = list(input())
    ans = ''
    for i in range(len(word)):
        if word[i] not in vowel:
            ans += word[i]
    print('#{} {}'.format(tc,ans))
# print(*vowel)
# print(''.join(vowel))
# print(''.join(map(str,vowel)))