code = { 0:'0001101',
         1:'0011001',
         2:'0010011',
         3:'0111101',
         4:'0100011',
         5:'0110001',
         6:'0101111',
         7:'0111011',
         8:'0110111',
         9:'0001011'}
def is_valid(data):
    check_code = []
    for i in range(0,len(data),7):
        new_data = data[i:i+7]
        tmp_data = ''
        for num in new_data:
            tmp_data+=str(num)
        for j in code:
            if code[j] == tmp_data:
                check_code.append(j)
    return check(check_code)

def check(data):
    res = 0
    for i in range(7):
        if i % 2:
            res += data[i]
        else:
            res += data[i] * 3
    res += data[-1]
    if not res % 10:
        return sum(data)
    else:
        return 0
for tc in range(int(input())):
    N, M = map(int,input().split())
    secret = [list(map(int,input())) for _ in range(N)]
    ans = 0
    for i in range(N):
        if sum(secret[i][:]) == 0:
            continue
        else:
            for j in range(M-1,-1,-1):
                if secret[i][j] != 0:
                    tmp = secret[i][j-55:j+1]
                    ans = is_valid(tmp)
                    break
    print('#{} {}'.format(tc+1,ans))
