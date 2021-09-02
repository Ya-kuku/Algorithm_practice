def solution(sticker):
    n = len(sticker)

    if n <= 3:
        return max(sticker)
    dp1 = [0 for _ in range(n)]
    dp2 = [0 for _ in range(n)]

    # 첫번째 스티커를 사용, 두번째칸은 첫번째 스티커의 사용값과 같음
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]

    # 첫번째 스티커를 사용했으니 마지막 스티커는 사용할 수 없음(원형스티커 이므로)
    for i in range(2,n-1):
        # 해당 인덱스의 스티커를 사용하는건 두번째 전까지의 합
        # 해당 스티커를 사용하지 않고 i-1칸까지의 합과 비교 해서 큰값이 해당 인덱스의 max값이 된다.
        dp1[i] = max(dp1[i-2] + sticker[i], dp1[i-1])

    # 두번째 스티커를 사용, 첫번째 디피 값은 0, 두번째 디피 값은 두번째 스티커 값과 같음
    dp2[0] = 0
    dp2[1] = sticker[1]

    # 두번째 스티커부터 사용하면 마지막 스티커는 사용이 가능
    for i in range(2,n):
        # 위의 설명과 같음
        dp2[i] = max(dp2[i-2] + sticker[i], dp2[i-1])

    return max(max(dp1),max(dp2))
solution([14,6,5,11,3,9,2,10])