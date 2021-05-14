n = int(input())
switch = list(input().split())
students = int(input())
for _ in range(students):
    sex, num = map(int,input().split())
    print(switch)
    if sex == 1:
        for i in range(num-1,n,num):
            if switch[i] == '1':
                switch[i] = '0'
            else:
                switch[i] = '1'
    else:
        st,ed = num-1,num-1
        if switch[num-1] == '1':
            switch[num-1] = '0'
        else:
            switch[num-1] = '1'
        while st >=0 and ed < n:
            if switch[st] == switch[ed]:
                if switch[st] == '1':
                    switch[st],switch[ed] = '0','0'
                else:
                    switch[st], switch[ed] = '1', '1'
                st-=1
                ed+=1
            else:
                break
print(switch)

