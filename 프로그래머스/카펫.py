def solution(brown, red):
    for index in range(1,red+1):
        # 내부 red의 사각형 크기를 찾기 위함
        if red%index == 0:
            length = red//index
            if (((index+2)*(length+2))-(index*length)) == brown:
                return [max(index+2,length+2),min(index+2,length+2)]