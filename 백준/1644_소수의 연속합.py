n = int(input())

seive = [True] * (n+1)

for i in range(2,int((n+1)**0.5)+1):
    if seive[i]:
        for j in range(2*i,n+1,i):
            seive[j] = False
prime_nums = []
for i in range(2,n+1):
    if seive[i]:
        prime_nums.append(i)

st = ed = 0
Sum_prime = 0
ans = 0
while 1:
    if Sum_prime >= n:
        if Sum_prime == n:
            ans += 1
        Sum_prime -= prime_nums[st]
        st += 1
    elif ed == len(prime_nums):
        break
    else:
        Sum_prime += prime_nums[ed]
        ed += 1

print(ans)


