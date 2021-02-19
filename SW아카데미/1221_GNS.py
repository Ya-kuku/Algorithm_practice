diff = {'ZRO':0,'ONE':1,'TWO':2,'THR':3,'FOR':4,'FIV':5,'SIX':6,'SVN':7,'EGT':8,'NIN':9}
diff_rev = {v:k for k,v in diff.items()}
# value값으로 key값 뽑아낼 때, 기존 dict을 뒤집거나 밑에처럼 하나씩 순회해서 찾기
# [k for k, v in aa.items() if v == 'CC']
# print(list(v for k,v in diff.items()))
for tc in range(int(input())):
    T,N = map(str,input().split())
    n = int(N)
    sen = list(map(str,input().split()))
    for i in range(n):
        sen[i] = diff[sen[i]]
    sen.sort()
    for i in range(n):
        sen[i] = diff_rev[sen[i]] 
    print('{}'.format(T),end=' ')
    print(*sen)
