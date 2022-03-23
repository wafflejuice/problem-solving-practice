def solution(cacheSize, cities):
    answer = 0
    for ci in range(len(cities)):
        cities[ci] = cities[ci].lower()
    answer = do(cacheSize, cities)
    return answer

def do(cacheSize, cities):
    cache = []
    cost = 0
    for ci in range(len(cities)):
        if cities[ci] in cache:
            cost += 1
            cache = update_cache(cache, cacheSize, True, cities[ci])
        else:
            cost += 5
            cache = update_cache(cache, cacheSize, False, cities[ci])
    return cost

def update_cache(cache, cacheSize, hit, new_elem):
    if hit:
        cache.remove(new_elem)
        cache.append(new_elem) # 뒤가 recent
    else:
        if len(cache) < cacheSize:
            cache.append(new_elem)
        else:
            cache.append(new_elem)
            cache = cache[1:]
    return cache



print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))

# 15분 미만