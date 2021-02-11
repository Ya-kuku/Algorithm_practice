def mergesort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    # 리스트를 계속 쪼갬
    left = mergesort(data[:mid])
    right = mergesort(data[mid:])

    i = j = 0
    result = []
    # 인덱스를 0부터하는 이유는 left와 right가 쪼갠 리스트를 계속 포함시키면서 병합
    # 이 상황에서 각각 리스트에 담긴 숫자를 앞에서부터 서로 비교하면서 새로운 result 결과값에 담아주기 위해 인덱스를 초기화
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
nums = list(map(int,input()))
print(*mergesort(nums)[::-1], sep='')

