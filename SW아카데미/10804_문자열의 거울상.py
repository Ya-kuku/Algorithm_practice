mirror = {'b':'d','d':'b','p':'q','q':'p'}
for tc in range(int(input())):
    sen = input()
    res = ''
    for i in range(len(sen)-1,-1,-1):
        res += mirror[sen[i]]
    print('#%d %s' %(tc+1,res))