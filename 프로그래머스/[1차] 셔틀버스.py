# n 배차횟수, t 배차시간, m 인원
def solution(n,t,m,timetable):
    answer = ''
    crew = [ int(tt.split(':')[0])*60 + int(tt.split(':')[1]) for tt in timetable]
    crew.sort()

    bus_time = [540+ (t*i) for i in range(n)]

    idx = 0
    for bus in bus_time:
        cnt = 0
        '''
        버스에 자리가 남음
        탑승할 크루가 남음
        해당 크루 버스 도착 시간 전 도착
        '''
        while cnt < m and idx < len(crew) and crew[idx] <= bus:
            idx += 1
            cnt += 1
        # 탑승인원 남았으니 버스시간이 콘의 탑승시간
        if cnt < m:
            answer = bus
        else:
            # 마지막 탑승 인원보다 1분전 시간
            answer = crew[idx-1] - 1

    return str(answer // 60).zfill(2) + ":" + str(answer % 60).zfill(2)

print(solution(2,1,2,["09:00", "09:00", "09:00", "09:00"]))