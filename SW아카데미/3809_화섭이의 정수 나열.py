for tc in range(int(input())):
    N = int(input())
    lst = []
    while len(lst) < N:
        lst += list(map(str, input().split()))
    new = ''.join(lst)

    for i in range(1000):
        if str(i) not in new:
            print("#{} {}".format(tc + 1, i))
            break

