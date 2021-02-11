# def split(data):
#     medium = int(len(data)/2)
#     left = data[:medium]
#     right = data[medium:]


def mergesplit(data):
    if len(data) <= 1:
        return data
    medium = int(len(data)/2)
    left = mergesplit(data[:medium])
    right = mergesplit(data[medium:])
    return merge(left, right)

def merge(left, right):
    merged = list()
    left_P, right_P = 0,0

    # case1 left/right 아직 남아있을 때

    while len(left) > left_P and len(right) > right_P:
        if left[left_P] > right[right_P]:
            merged.append(right[right_P])
            right_P += 1
        else:
            merged.append(left[left_P])
            left_P += 1

    # case2 left 만 남아있을 때
    while len(left) > left_P:
        merged.append(left[left_P])
        left_P += 1

    # case2 right 남아있을 때
    while len(right) > right_P:
        merged.append(right[right_P])
        right_P += 1

    return merged

print(mergesplit([1,6,2,3,8,5,2,3,12]))