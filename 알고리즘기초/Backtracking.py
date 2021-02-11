def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] -current_col) == current_row - queen_row:
            return False
        return True

def dfs(N, current_row, current_candidtae,final_result):
    if current_row == N:
        final_result.append(current_candidtae[:])
        return

    for candidate_col in range(N):
        # 새로운 행에서 후보군들 중에 가능한 후보군이 있는지
        if is_available(current_candidtae,candidate_col):
            current_candidtae.append(candidate_col)
            dfs(N, current_row+1, current_candidtae, final_result)
            # 추가한 후보군이 불가능한 경우 pop
            current_candidtae.pop()

def nqueens(N):
    final_result = []
    dfs(N,0,[],final_result)
    return final_result