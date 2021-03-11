def solution(arr1, arr2):
    a = len(arr1)
    b = len(arr2[0])
    answer = [[0] * b for _ in range(a)]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += (arr1[i][k] * arr2[k][j])

    return answer

def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

print(productMatrix([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]]))