birds = int(input())

sec = 0
st = 1
now = birds
while now != 0:
    if now < st:
        st = 1
    else:
        now -= st
        sec += 1
        st += 1
print(sec)