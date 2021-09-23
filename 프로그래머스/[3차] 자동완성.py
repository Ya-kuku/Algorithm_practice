from collections import defaultdict
def make_trie(words):
    trie = defaultdict()
    for word in words:
        cur_dict = trie
        for letter in word:
            if letter not in cur_dict:
                cur_dict[letter] = ([0,{}])
                cur_dict[letter][0] += 1
            else:
                cur_dict[letter][0] += 1
            cur_dict = cur_dict[letter][1]
            # cur_dict.setdefault(letter,[0,dict()])
            # cur_dict[letter][0] += 1
            # cur_dict = cur_dict[letter][1]
    print(trie)
    return trie

def solution(words):
    answer = 0
    trie = make_trie(words)
    for word in words:
        tmp = trie
        for letter in word:
            answer += 1
            tmp = tmp[letter]
            if tmp[0] == 1:
                break
            else:
                tmp = tmp[1]
    print(answer)
    return answer

solution(["go","gone","guild"])