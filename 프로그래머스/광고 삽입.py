def solution(play_time, adv_time, logs):
    n = len(logs)
    logs = [log.split('-') for log in logs]
    times = [[] for _ in range(n)]
    for j in range(len(logs)):
        for i in range(2):
            tmp_time = logs[j][i].split(':')
            res = int(tmp_time[0]) * 3600 + int(tmp_time[1]) * 60 + int(tmp_time[2])
            times[j].append(res)
    times.sort()
    ad_time = int(adv_time[:2]) * 3600 + int(adv_time[3:5]) * 60 + int(adv_time[6:])

    answer = []

    if play_time == adv_time:
        return "00:00:00"
    else:
        for i in range(len(times)):
            start_time = times[i][0]
            end_time = start_time + ad_time
            cnt = 0
            for j in range(len(times)):
                if times[j][0] == start_time:
                    if times[j][1] < end_time:
                        cnt += times[j][1] - times[j][0]
                    else:
                        cnt += ad_time
                else:
                    # 광고끝나는 시간보다 시작시간이 늦으면 패스
                    if times[j][0] > end_time: continue
                    # 광고시작시간보다 끝나는 시간이 늦으면 패스
                    elif start_time > times[j][1]: continue
                    # 광고시작시간보다 시작시간이 빠르고, 광고 끝나는 시간보다 끝나는 시간이 느리면 광고 전체 포함
                    elif times[j][0] <= start_time and times[j][1] >= end_time:
                        cnt += ad_time
                    # 광고시작시간보다 시작시간은 빠르고, 광고 끝나는 시간보다 끝나는 시간이 빠르면 광고시작시간부터 끝나는 시간까지
                    elif times[j][0] <= start_time and times[j][1] < end_time:
                        cnt += times[j][1] - start_time
                    # 광고시작시간보다 시작시간은 느리고, 광고 끝나는 시간보다 끝나는 시간이 느리면 시작시간부터 광고끝나는 시간까지
                    elif times[j][0] > start_time and times[j][1] >= end_time:
                        cnt += end_time - times[j][0]
                    else: continue

            answer.append([start_time,cnt])

    answer.sort(key=lambda data:(data[1],-data[0]))
    tmp = answer[-1][0]
    res = ""
    a = tmp // 3600
    b = (tmp - (a * 3600)) // 60
    c = tmp - (a * 3600 + b * 60)
    if len(str(a)) == 1:
        res += "0" + str(a) + ":"
    else:
        res += str(a) + ":"
    if len(str(b)) == 1:
        res += "0" + str(b) + ":"
    else:
        res += str(b) + ":"
    if len(str(c)) == 1:
        res += "0" + str(c)
    else:
        res += str(c)

    return res
def solution(play_time, adv_time, logs):
    play_time = str_to_int(play_time)        # 1
    adv_time = str_to_int(adv_time)
    all_time = [0 for i in range(play_time + 1)]

    for l in logs:                           # 2
        start, end = l.split('-')
        start = str_to_int(start)
        end = str_to_int(end)
        all_time[start] += 1
        all_time[end] -= 1

    for i in range(1, len(all_time)):       # 3
        all_time[i] = all_time[i] + all_time[i - 1]

    for i in range(1, len(all_time)):       # 4
        all_time[i] = all_time[i] + all_time[i - 1]

    most_view = 0                           # 5
    max_time = 0
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < all_time[i] - all_time[i - adv_time]:
                most_view = all_time[i] - all_time[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < all_time[i]:
                most_view = all_time[i]
                max_time = i - adv_time + 1

    return int_to_str(max_time)


def str_to_int(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def int_to_str(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s
solution("02:03:55","00:14:15",
         ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])