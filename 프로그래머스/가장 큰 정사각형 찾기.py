# def solution(board):
#     row = len(board)
#     col = len(board[0])
#     for i in range(row):
#         for j in range(col):
#             if i == 0 or j == 0:
#                 continue
#             if board[i][j] != 0:
#                 board[i][j] = min(board[i-1][j-1],min(board[i-1][j],board[i][j-1]))+1
#     answer=[]
#     for i in range(row):
#         answer.append(max(board[i]))
#     return max(answer)**2
import sys
def solution(board):
    answer = 0
    row = len(board)
    col = len(board[0])
    # 사각형 크기
    for k in range(min(row,col),0,-1):
        # 자른 사각형 범위
        for i in range(row-k+1):
            for j in range(col-k+1):
                # 사각형 탐색
                flag = False
                for p in range(i,i+k):
                    for q in range(j,j+k):
                        if board[p][q] != 1:
                            flag = True
                            break
                    if flag:
                        break
                else:
                    answer = k
                    return answer ** 2

    return answer**2
