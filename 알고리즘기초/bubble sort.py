# def bubble(data):
#     for i in range(len(data)-1):
#         for j in range(len(data)-1-i):
#             if data[j] > data[j+1]:
#                 data[j], data[j+1] = data[j+1], data[j]
#     return data
# a = [1,123,4,2,7,5,11,8,9]
# print(bubble(a))

import random
def bubblesort(data):
    for i in range(len(data)-1):
        swap = False
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swap = True
        # 정렬이 다 된후에 다시 순회하는걸 막아주는 코드, 시간 줄이기
        if swap == False:
            break
    return data

data_list = random.sample(range(100),8)
print(data_list)
print(bubblesort(data_list))