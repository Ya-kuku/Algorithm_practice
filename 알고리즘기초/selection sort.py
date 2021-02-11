import random
def selectionsort(data):
    for i in range(len(data) - 1):
        Min = i
        for j in range(i+1,len(data)):
            if data[Min] > data[j]:
                Min = j
        # 최초의 기준점과 자리를 바꾸기 때문에 i의 값과 자리 swap
        data[Min], data[i] = data[i], data[Min]
    return data

data_list = random.sample(range(100),10)

print(selectionsort(data_list))


