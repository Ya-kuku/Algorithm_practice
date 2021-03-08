n = int(input())
money = [500,100,50,10,5,1]
tmp = 1000 - n
cnt = 0
for i in money:
    cnt += tmp // i
    tmp %= i
print(cnt)