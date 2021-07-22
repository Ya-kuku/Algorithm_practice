from collections import defaultdict

def insert(trie, word):
    curr = trie
    while word:
        s = word[0]
        if s not in curr:
            curr[s] = [0, {}]
        curr[s][0] += 1
        curr = curr[s][1]
        word = word[1:]


def find(trie, query):
    v = 0
    curr = trie
    if len(trie) == 0:
        return 0

    while query:
        if query[0] == "?":
            return v
        else:
            if query[0] not in curr:
                return 0
            v = curr[query[0]][0]
            curr = curr[query[0]][1]
        query = query[1:]
    return v


def solution(words, queries):
    ans = []
    trie = defaultdict(dict)
    rev_trie = defaultdict(dict)
    len_dict = defaultdict(int)

    for word in words:
        insert(trie[len(word)], word)
        insert(rev_trie[len(word)], word[::-1])
        len_dict[len(word)] += 1

    for q in queries:
        lq = len(q)
        if q[0] == "?" and q[-1] == "?":
            ans.append(len_dict[lq])
        elif q[-1] == "?":
            ans.append(find(trie[lq], q))
        elif q[0] == "?":
            ans.append(find(rev_trie[lq], q[::-1]))

    return ans

solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"])