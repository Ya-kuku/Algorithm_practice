def comb(lst, n):
    ret = []
    if n > len(lst): return ret

    if n == 1:
        for i in lst:
            ret.append([i])
    elif n > 1:
        for i in range(len(lst) - n + 1):
            for temp in comb(lst[i + 1:], n - 1):
                ret.append([lst[i]] + temp)

    return ret

items = [1,2,3,4,5]
print(comb(items,2))
# def perm(lst,n):
# 	ret = []
# 	if n > len(lst): return ret
#
# 	if n==1:
# 		for i in lst:
# 			ret.append([i])
# 	elif n>1:
# 		for i in range(len(lst)):
# 			temp = [i for i in lst]
# 			temp.remove(lst[i])
# 			for p in perm(temp,n-1):
# 				ret.append([lst[i]]+p)
#
# 	return ret


def dfs_comb(lst, n):
    ret = []
    idx = [i for i in range(len(lst))]

    stack = []
    for i in idx[:len(lst) - n + 1]:
        stack.append([i])

    while len(stack) != 0:
        cur = stack.pop()

        for i in range(cur[-1] + 1, len(lst) - n + 1 + len(cur)):
            temp = cur + [i]
            if len(temp) == n:
                element = []
                for i in temp:
                    element.append(lst[i])
                ret.append(element)
            else:
                stack.append(temp)
    return ret

ls = [1,2,3,4]
def combinationz(ls, n):
    ret = []
    if n == 0 or n>len(ls):
        pass
    elif n == 1:
        ret += list(map(lambda x:{x}, ls))
    else:
        for i in range(len(ls)):
            ret += list(map(lambda x: {ls[i]}|x, combinationz(ls[i+1:], n-1)))
    return ret

def permutationz(ls, n):
    ret = []
    if n == 0 or n>len(ls):
        return ret
    elif n == 1:
        return list(map(lambda x:(x,), ls))
    else:
        for i in range(len(ls)):
            temp = [e for e in ls]
            temp.remove(ls[i])
            ret += tuple(map(lambda x: (ls[i], ) + x ,permutationz(temp, n-1)))
    return ret


print(combinationz(ls, 2))
print(permutationz(ls, 2))

