def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    j = 0

    for i in range(len(A)):
        if A[j] < B[i]:
            answer += 1
            j += 1

    return answer
solution([5,1,3,7],[2,2,6,8])