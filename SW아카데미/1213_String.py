for tc in range(10):
    T = int(input())
    word = input()
    sentence = input()
    ans = 0
    for i in range(len(sentence)-len(word)+1):
        if sentence[i] == word[0]:
            if sentence[i:i+len(word)] == word:
                ans += 1
    print('#{} {}'.format(T,ans))