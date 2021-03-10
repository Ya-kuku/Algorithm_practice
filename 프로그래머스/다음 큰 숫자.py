def solution(n):
    bin_num = bin(n).count('1')
    for i in range(n+1,1000001):
        if bin(i).count('1') == bin_num:
            return i

print(solution(78))
a = [1101]