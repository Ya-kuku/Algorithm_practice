matchs = [6,2,5,5,4,5,6,3,7,6]
ans=[0, 0, 1, 7, 4, 2, 6, 8, 10, 18, 22]
for _ in range(int(input())):
    n = int(input())
    Max = '7' * (n%2) + '1'*(n//2-(n%2))
    Min = ''
    if n <= 10:
        Min = ans[n]
        print(Min, Max)
        continue

    while n >0:
        n -= 7
        if n >= 0:
            Min += '8'
        else:
            n += 7
            break

    small = {6: 6, 2: 1, 5: 2}
    if n in small:
        Min = str(small[n]) + Min
    else:
        if n == 1:
            Min = '10' + Min[1:]
        elif n == 3:
            Min = '200' + Min[2:]
        elif n == 4:
            Min = '20' + Min[1:]

    print(Min, Max)