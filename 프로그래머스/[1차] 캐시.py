def solution(cacheSize, cities):
    cities = [i.lower() for i in cities]
    answer = 5
    cache = [cities[0]]
    if cacheSize == 0:
        answer += 5 * (len(cities) -1)
    else:
        for i in cities[1:]:
            if len(cache) < cacheSize and i in cache:
                cache.pop(cache.index(i))
                answer += 1
            elif len(cache) < cacheSize:
                answer += 5
            elif i in cache:
                cache.pop(cache.index(i))
                answer += 1
            else:
                del cache[0]
                answer += 5
            cache.append(i)
    return answer


solution(5,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])