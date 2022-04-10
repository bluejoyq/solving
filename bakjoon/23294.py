
class Web:
    def __init__(self, max_cache_size, size_of_page):
        from collections import deque
        self.front = []
        self.back = deque([])
        self.cur = None
        self.cache_size = 0
        self.max_cache_size = max_cache_size
        self.size_of_page=  size_of_page
    def backward(self):
        if len(self.back) == 0:
            return
        
        self.front.append(self.cur)
        self.cur = self.back.pop()
    
    def frontward(self):
        if len(self.front) == 0:
            return 
        
        self.back.append(self.cur)
        self.cur = self.front.pop()

    def access(self, target):
        while self.front:
            self.change_cache_size(self.front.pop(), -1)
        
        if self.cur:
             self.back.append(self.cur)

        self.cur = target
        self.change_cache_size(self.cur)


    def change_cache_size(self, page_num, flag = 1):
        self.cache_size += flag *self.size_of_page[page_num]
        while self.cache_size > self.max_cache_size:
            self.cache_size -= self.size_of_page[self.back.popleft()]
    
    def compress(self):
        from collections import deque
        visited = [0] * len(self.size_of_page)
        new_back = deque([])
        while len(self.back):
            b = self.back.pop()
            if visited[b]:
                self.change_cache_size(b, -1)
                continue
            visited[b] = 1
            new_back.appendleft(b)
        self.back = new_back


def solve():
    import sys
    input = sys.stdin.readline
    N,Q,C = map(int, input().split())
    values = [0] + list(map(int,input().split()))
    web = Web(C, values)

    for i in range(Q):
        comms = list(input().split())
        if len(comms) > 1:
            web.access(int(comms[1]))
        elif comms[0] == 'B':
            web.backward()
        elif comms[0] == 'F':
            web.frontward()
        else:
            web.compress()

    print(web.cur)
    
    if len(web.back) == 0:
        print(-1)
    else:
        result = ''
        while web.back:
            result += str(web.back.pop()) + ' '
        print(result)
           
    if len(web.front) == 0:
        print(-1)
    else:
        result = ''
        while web.front:
            result += str(web.front.pop()) + ' '
        print(result)

solve()