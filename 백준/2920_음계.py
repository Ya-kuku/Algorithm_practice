data = list(map(int,input().split()))
tmp = sorted(data)
ans = 'mixed'

if data == tmp:
    ans = 'ascending'
elif data == tmp[::-1]:
    ans = 'descending'

print(ans)


