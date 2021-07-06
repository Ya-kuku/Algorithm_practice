def secret(n,lst,arr):

    for idx in range(n):
        binary = bin(lst[idx])[2:]
        if len(binary) < n:
            tmp_num = n - len(binary)
            binary = '0'* tmp_num + binary
        print(binary)
        for i in range(n):
            if binary[i] == '1':
                if arr[idx][i] == '.':
                    arr[idx][i] = '#'

def solution(n, arr1, arr2):
    answer = []
    arr = [['.'] * n for _ in range(n)]
    secret(n,arr1,arr)
    print(arr)
    secret(n,arr2,arr)

    for ar in arr:
        tmp_ar = ''
        for i in range(n):
            if ar[i] == '#':
                tmp_ar += '#'
            else:
                tmp_ar += ' '
        answer.append(tmp_ar)
    print(answer)
    return answer

solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10])

