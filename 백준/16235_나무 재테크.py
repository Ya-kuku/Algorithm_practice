from collections import deque
dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]
n,m,k = map(int,input().split())
bob = [list(map(int,input().split())) for _ in range(n)]
nutri = [[5] * n for _ in range(n)]
trees = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x,y,age = map(int,input().split())
    trees[x-1][y-1].append(age)

def spring():
    for i in range(n):
        for j in range(n):
            die_trees = []
            if trees[i][j]:
                # 나무가 여러개일 경우
                if len(trees[i][j]) > 1:
                    trees[i][j].sort()
                    impos_cnt = 0
                    for b in range(len(trees[i][j])):
                        if nutri[i][j] >= trees[i][j][b]:
                            nutri[i][j] -= trees[i][j][b]
                            trees[i][j][b] += 1
                        else:
                            impos_cnt +=1
                            die_trees.append(trees[i][j][b])
                    # 리스트 슬라이싱으로 자르는거 비교 trees[i][j][b:b+pos_cnt]
                    trees[i][j] =  trees[i][j][:len(trees[i][j]) - impos_cnt]
                    # for _ in range(impos_cnt):
                    #     trees[i][j].pop()

                # 나무가 한개일 경우
                else:
                    if nutri[i][j] >= trees[i][j][0]:
                        nutri[i][j] -= trees[i][j][0]
                        trees[i][j][0] += 1
                    else:
                        die_trees.append(trees[i][j][0])
                        trees[i][j].pop()
            else: continue
            # 죽은 나무 양분추가
            for die in die_trees:
                nutri[i][j] += die // 2
def autumn():
    for i in range(n):
        for j in range(n):
            nutri[i][j] += bob[i][j]
            if trees[i][j]:
                for a in range(len(trees[i][j])):
                    # 나무의 나이가 5의 배수인 경우
                    if trees[i][j][a] % 5 == 0:
                        for b in range(8):
                            ni = i + dr[b]
                            nj = j + dc[b]
                            if 0<= ni < n and 0 <= nj <n:
                                trees[ni][nj].append(1)
            else:continue


for _ in range(k):
    spring()
    autumn()

alive_trees = 0
for i in range(n):
    for j in range(n):
        if trees[i][j]:
            alive_trees += len(trees[i][j])
print(alive_trees)

