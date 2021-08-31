from itertools import *
def solution(word):
    answer = 0
    vowels= ['A','E','I','O','U']
    # tmp = list(map(''.join,permutations(vowels,3)))
    # print(tmp)
    # for i in range(1,6):
    #     tmp = list(map(' '.join, product(['A', 'E', 'I', 'O', 'U'], repeat=i)))
    #     print(tmp)
    words = []
    for i in range(5):
        tmp_word = ''
        tmp_word += vowels[i]
        words.append(tmp_word)
        for j in range(5):
            tmp_word = ''
            tmp_word += vowels[i] + vowels[j]
            words.append(tmp_word)
            for x in range(5):
                tmp_word = ''
                tmp_word += vowels[i] + vowels[j] + vowels[x]
                words.append(tmp_word)
                for y in range(5):
                    tmp_word = ''
                    tmp_word += vowels[i] + vowels[j] + vowels[x] + vowels[y]
                    words.append(tmp_word)
                    for k in range(5):
                        tmp_word = ''
                        tmp_word += vowels[i] +vowels[j] + vowels[x] + vowels[y] + vowels[k]
                        words.append(tmp_word)

    print(words.index(word) + 1)
solution("I")