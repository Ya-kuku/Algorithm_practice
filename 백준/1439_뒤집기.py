n = input()
cnt0 = 0
cnt1 = 0
if n[0] == '0':
    cnt0 += 1
else:
    cnt1 += 1

for i in range(len(n)-1):
    if n[i] != n[i+1]:
        if n[i+1] == '0':
            cnt0 += 1
        else:
            cnt1 += 1

print(min(cnt0,cnt1))