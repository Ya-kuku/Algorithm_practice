for t in range(1, int(input()) + 1):
    string = list(input())
    H = int(input())
    pos = sorted(list(map(int, input().split())), reverse=True)
    for idx in pos:
        string.insert(idx, '-')
    print('#{} {}'.format(t, ''.join(string)))