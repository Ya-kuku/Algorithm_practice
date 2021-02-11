for tc in range(10):
    length = int(input())
    palindrome = [list(input()) for _ in range(8)]
    ans = 0
    for i in range(8):
        for j in range(8-length+1):
            tmp = []
            tmp.extend(palindrome[i][j:j+length])
            if tmp == tmp[::-1]:
                ans += 1
    for i in range(8):
        for j in range(8-length+1):
            tmp = []
            for k in range(length):
                tmp.append(palindrome[j+k][i])
            if tmp == tmp[::-1]:
                ans += 1
    print("#{} {}".format(tc+1,ans))

