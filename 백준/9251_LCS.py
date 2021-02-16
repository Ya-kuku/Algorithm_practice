A = input()
B = input()
dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
# 문자열을 하나씩 늘려줄 때, 하나씩 비교하는 것 같지만 그 이전까지 문자열 비교값을 dp에 담아두었기 때문에
# 만약에 해당 인덱스에서 문자열이 같은 경우에는 그 이전 대각선 값까지 문자열이 같았다는 뜻이고
# 현재 인덱스에서 문자열이 같으니 +1을 해준다
# 그런 경우가 아니면은 그 이전 위, 아래 부분에서 max 값을 담아주면서 dp 쌓아간다
for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[len(A)][len(B)])
