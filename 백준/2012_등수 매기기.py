n = int(input())
score = [(i,int(input())) for i in range(n)]
score.sort(key= lambda data : data[1])
ans = 0
for i in range(n):
    ans += abs(score[i][1] - (i+1))
print(ans)
