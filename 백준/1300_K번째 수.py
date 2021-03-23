# k 번째수는 k보다 작거나 같음 ex) 3 * 3 = 1,2,2,3,3,4,6,6,7
# idx가 1,2,3 일때 모든 수는 작거나 같다
# 따라서 k보다 작은 수의 갯수를 구하면 답을 알 수 있음
def binSearch(start, end, n, k):
    while start <= end:
        mid = (start + end) // 2

        cnt = 0
        for i in range(1,n+1):
            cnt += min(mid // i, n)

        if cnt >= k:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer

n = int(input())
k = int(input())

print(binSearch(1, n*n, n, k))