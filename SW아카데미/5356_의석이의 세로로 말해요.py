from itertools import zip_longest

for tc in range(int(input())):
    words = [input() for _ in range(5)]
    zipped = zip_longest(*words)
    print('#{}'.format(tc+1),end=' ')
    for i in zipped:
        print(''.join(filter(None,i)),end='')
    print()