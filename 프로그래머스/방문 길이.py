dir = {'U':(-1,0),'D':(1,0),'R':(0,1),'L':(0,-1)}

def solution(dirs):
    answer = 0
    visited = set()
    x,y = 5,5
    for i in range(len(dirs)):
        nx = x + dir[dirs[i]][0]
        ny = y + dir[dirs[i]][1]
        if nx < 0 or nx >= 11 or ny < 0 or ny >= 11: continue
        if (x,y,nx,ny) not in visited:
            visited.add((x,y,nx,ny))
            # 걸어간 길은 양방향성을 고려
            visited.add((nx,ny,x,y))
            answer += 1
        x = nx
        y = ny

    return answer

print(solution("ULURRDLLU"))