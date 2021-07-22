from collections import defaultdict
def insert(trie, num):
    cur = trie
    while num:
        st = num[0]
        if st not in cur:
            cur[st] = {}
        cur = cur[st]
        num = num[1:]

def find(trie,num):
    cur = trie

    while num:
        if len(num) == 1 and cur[num[0]]:
            return False

        cur = cur[num[0]]
        num = num[1:]
    return True

for tc in range(int(input())):
    n = int(input())
    phone_numbers = []
    for _ in range(n):
        phone_numbers.append(input())

    trie = defaultdict(dict)

    for number in phone_numbers:
        insert(trie,number)

    phone_numbers.sort()
    for number in phone_numbers:
        if not find(trie,number):
            print('NO')
            break
    else:
        print('YES')

