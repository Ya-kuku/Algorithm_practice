def rotate(key):
    rotate_key = [[0] * len(key) for _ in range(len(key))]
    for i in range(len(key)):
        for j in range(len(key)):
            rotate_key[j][len(key)-1-i] = key[i][j]
    return rotate_key

def check(key,lock,st_i,st_j,end):
    length = (len(key) * 2) + len(lock) - 2
    background = [[0] * length for _ in range(length)]

    # 자물쇠 정보 입력
    for i in range(len(lock)):
        for j in range(len(lock)):
            background[(length-len(lock))//2+i][(length-len(lock))//2+j] += lock[i][j]

    # 키 값 입력
    for i in range(len(key)):
        for j in range(len(key)):
            background[st_i+i][st_j+j] += key[i][j]

    # 입력 받은 값 자물쇠 범위만큼 확인하기
    for i in range(len(lock)):
        for j in range(len(lock)):
            if background[(length - len(lock)) // 2 + i][(length - len(lock)) // 2 + j] != 1:
                return False
    return True

def solution(key, lock):
    # 키가 들어갈 수 있는 곳까지의 범위
    span = len(key) + len(lock) - 1
    # 행렬 돌리는 횟수
    for _ in range(4):
        for i in range(span):
            for j in range(span):
                if check(key,lock,i,j,span):
                    return True
        key = rotate(key)

    return False