# 13분
# [1차] 캐시 https://programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize, cities):
    from collections import deque
    answer = 0
    cache = deque([])
    for city in cities:
        city = city.upper()
        try:
            # cache hit
            idx = cache.index(city)
            del cache[idx]
            cache.append(city)
            answer += 1
        except:

            answer += 5
            if cacheSize > 0 and len(cache) == cacheSize:

                cache.popleft()
                cache.append(city)
            elif cacheSize > 0:
                cache.append(city)
        
            
        
            
    
    return answer