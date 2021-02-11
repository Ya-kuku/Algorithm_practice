def mergesort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2

    left = mergesort(data[:mid])
    right = mergesort(data[mid:])

    i = j = 0
    res = []
    while i < len(left) and j < len(right):
        # i와 j의 인덱스로 비교 했을 때, 인덱스가 0인 상황에서 두 리스트에서 작은 값을 먼저 넣어주고
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    # 이 상황에서는 아무조건에도 포함되지 않으니 숫자가 차례대로 나열되어 있어 차례대로 포함시켜 줌
    res += left[i:]
    res += right[j:]
    return res

nums = []
for _ in range(int(input())):
    nums.append(int(input()))

print(*mergesort(nums), sep='\n')