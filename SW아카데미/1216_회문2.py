for _ in range(10):
    tc = int(input())
    array = [list(input()) for _ in range(100)]
    Max = 0
    for k in range(2,101):
        for i in range(100):
            for j in range(100):
                palindrome = array[i][j:j+k]
                if palindrome == palindrome[::-1]:
                    Max = max(len(palindrome),Max)

    for i in range(100):
        for j in range(100):
            palindrome = []
            for k in range(100):
                idx = j + k
                if idx >= 100: break
                else:
                    palindrome.append(array[j+k][i])
                if palindrome == palindrome[::-1]:
                    Max = max(len(palindrome),Max)

    print('#{} {}'.format(tc,Max))