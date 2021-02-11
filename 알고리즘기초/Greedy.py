# 탐욕 알고리즘은 근사치 추정에 활용
# 반드시 최적의 해를 구하는 것 x

# 동전 문제
coin_list =[500,100,50,1]

def min_coin_count(value,coin_list):
    total_coin_count = 0
    details = list()
    coin_list.sort(reverse=True)
    for coin in coin_list:
        coin_num = value // coin
        total_coin_count += coin_num
        value -= coin_num * coin
        details.append([coin,coin_num])
    return total_coin_count, details

print(min_coin_count(4720,coin_list))

# 부분 배낭 문제
data_list =[(10,10),(15,12),(20,10),(25,8),(30,5)]

def get_max_value(data_list,capacity):
    data_list = sorted(data_list, key=lambda x: x[1] / x[0], reverse=True)
    print(data_list)
    total_value = 0
    details = list()

    for data in data_list:
        # 정렬한후에 제일 처음 데이터가 무게대비 가치가 가장 큰 경우이니 그냥 빼도 된다
        if capacity - data[0] >= 0:
            capacity -= data[0]
            total_value += data[1]
            # 1이라는 숫자는 몇 %를 넣었는지에 대한 비율 즉 100%
            details.append([data[0],data[1],1])
        else:
            # 허용치가 데이터의 크기보다 작은 경우 물건을 쪼개서 넣기
            fraction = capacity / data[0]
            total_value += data[1] * fraction
            details.append([data[0],data[1],fraction])
            break
    return total_value, details

print(get_max_value(data_list,30))