def solution(name):
    answer = 0
    alpa = [min(ord(i) - ord('A'),ord('Z') - ord(i) + 1) for i in name]
    idx = 0

    while 1:
        # 처음시작값은 무조건 첫번째에서 이동
        answer += alpa[idx]
        alpa[idx] = 0
        if not sum(alpa):
            return answer

        left,right = 1,1
        while alpa[idx-left] == 0:
            left += 1
        while alpa[idx+right] == 0:
            right += 1

        if left < right:
            answer += left
            idx += -left
        else:
            answer += right
            idx += right

    return answer

solution('JAZ')