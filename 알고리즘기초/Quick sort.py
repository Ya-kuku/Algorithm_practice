def qsort(data):
    if len(data) <= 1:
        return data

    # left, right = list(), list()
    # pivot = data[0]
    #
    # for index in range(1, len(data)):
    #     if pivot > data[index]:
    #         left.append(data[index])
    #     else:
    #         right.append(data[index])

    #이런식으로 바꿀수 있다
    pivot = data[0]

    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <= item]

    return qsort(left) + [pivot] + qsort(right)

import random
data_list = random.sample(range(100),10)

print(qsort(data_list))