from collections import deque
# from itertools import *
# def get_distance(x,y,dx,dy):
#     if x != dx and y != dy:
#         return 2
#     elif x == dx and y == dy:
#         return 0
#     else:
#         return 1
#
# def solution(board, r, c):
#     answer = 1e9
#     cards = dict()
#     for i in range(4):
#         for j in range(4):
#             if board[i][j]:
#                 if board[i][j] not in cards:
#                     cards[board[i][j]] = [(i,j)]
#                 else:
#                     cards[board[i][j]].append((i,j))
#
#     n = len(cards)
#     for card_num in permutations([x for x in range(1,n+1)],n):
#         # 현재 위치
#         x,y = r,c
#         move_cnt = 0
#
#         for num in card_num:
#             distance = []
#             # 해당 숫자의 카드의 위치
#             for dx, dy in cards[num]:
#                 result_dist = get_distance(x,y,dx,dy)
#                 # 거리값, x,y 좌표
#                 distance.append((result_dist,dx,dy))
#
#             # 두개의 카드 거리값 중 가까운 걸로 탐색
#             if distance[0][0] < distance[1][0]:
#                 move_cnt += distance[0][0]
#                 x,y = distance[0][1], distance[0][2]
#                 dx,dy = distance[1][1], distance[1][2]
#                 move_cnt += get_distance(x,y,dx,dy)
#                 x,y = dx, dy
#
#             else:
#                 move_cnt += distance[1][0]
#                 x, y = distance[1][1], distance[1][2]
#                 dx, dy = distance[0][1], distance[0][2]
#                 move_cnt += get_distance(x, y, dx, dy)
#                 x, y = dx, dy
#         answer = min(answer,move_cnt + n*2)
#     print(answer)
#     return answer
#
# solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0)

from collections import defaultdict, deque
from itertools import permutations
from copy import deepcopy
def move_cost(board, start, end):   # 조작 횟수 Count
    if start==end: return 0
    queue, visit = deque([[start[0], start[1], 0]]), {start}
    while queue:                    # BFS
        x, y, c = queue.popleft() 
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = x+dx, y+dy     # Normal move
            cx, cy = x, y
            while True:             # Ctrl + move
                cx, cy = cx+dx, cy+dy
                if not (0 <= cx <= 3 and 0 <= cy <= 3):
                    cx, cy = cx-dx, cy-dy
                    break
                elif board[cx][cy] != 0:
                    break

            if (nx, ny) == end or (cx, cy) == end:  # 도착 최단 경로
                return c+1

            if (0 <= nx <= 3 and 0 <= ny <= 3) and (nx, ny) not in visit:
                queue.append((nx, ny, c+1))
                visit.add((nx, ny))
            if (cx, cy) not in visit:
                queue.append((cx, cy, c+1))
                visit.add((cx, cy))

def cls_cost(board, cdict, curr, order, cost):
    if len(order)==0: return cost   # 모든 카드를 확인한 경우
    idx = order[0]+1                # 현재 선택해야할 카드의 종류

    # 현재위치에서 A1까지의 조작 횟수 + A1->A2까지의 조작 횟수 + 2(카드 선택)
    choice1 = move_cost(board, curr, cdict[idx][0]) + move_cost(board, cdict[idx][0], cdict[idx][1]) + 2
    choice2 = move_cost(board, curr, cdict[idx][1]) + move_cost(board, cdict[idx][1], cdict[idx][0]) + 2

    # 선택한 카드는 board에서 0으로 변경
    new_board = deepcopy(board)
    new_board[cdict[idx][0][0]][cdict[idx][0][1]] = 0
    new_board[cdict[idx][1][0]][cdict[idx][1][1]] = 0

    if choice1 < choice2:   # 적은 조작 횟수를 한 경우를 따라 재귀
        return cls_cost(new_board, cdict, cdict[idx][1], order[1:], cost + choice1)
    else:
        return cls_cost(new_board, cdict, cdict[idx][0], order[1:], cost + choice2)

def solution(board, r, c):
    answer = float('inf')
    cdict = defaultdict(list)
    for row in range(4):        # 카드의 종류에 따라 좌표 저장
        for col in range(4):
            num = board[row][col]
            if num != 0:
                cdict[num].append((row, col))

    for case in permutations(range(len(cdict)), len(cdict)):    # 완전 탐색
        answer = min(answer, cls_cost(board, cdict, (r, c), case, 0))

    return answer