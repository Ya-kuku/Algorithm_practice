def solution(m, musicinfos):
    answer = ''
    # 들은 멜로디
    stack = []
    for i in range(len(m)):
        if m[i] == '#':
            stack.append(stack.pop() + '#')
        else:
            stack.append(m[i])
    # 재생 된 곡들 정보
    stack_music = []
    idx = 0
    for music in musicinfos:
        # 각 곡 마다 재생된 정보
        temp = []
        music = music.split(',')
        for j in range(len(music[-1])):
            if music[-1][j] == '#':
                temp.append(temp.pop() + '#')
            else:
                temp.append(music[-1][j])
        # 현재곡 재생 시간, 정보 담기
        st_h, st_m = music[0].split(':')
        ed_h, ed_m = music[1].split(':')
        time = (int(ed_h) - int(st_h)) * 60 + (int(ed_m) - int(st_m))
        cur_music = []
        for k in range(time):
            idx = 0
            # 곡 하나 반복 됫는지
            if k >= len(temp):
                cur_music.append(temp[k%len(temp)])
            else:
                cur_music.append(temp[k])
        # idx, time, cur_music, music_name
        stack_music.append((idx, time, cur_music, music[2]))
        idx += 1
    ans = []
    for res in stack_music:
        for p in range(len(res[2])):
            if res[2][p] == stack[0]:
                tmp = res[2][p:p+len(stack)]
                if tmp == stack:
                    ans.append(res)
                    break

    ans.sort(reverse=True,key=lambda data: data[1])
    if not ans:
        answer = '(None)'
    elif len(ans) == 1:
        answer = ans[0][-1]
    else:
        answer = ans[0][-1]
    return answer

m = "CC#BCC#BCC#BCC#B"
b = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
print(solution(m,b))

