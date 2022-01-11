import sys
input = sys.stdin.readline


class Node:
    def __init__(self, val, nxt = None, bef = None):
        self.val = val
        self.nxt = nxt
        self.bef = bef
    def get_val(self):
        return self.val
    def get_nxt(self):
        return self.nxt
    def get_bef(self):
        return self.bef
    def set_bef(self, node):
        self.bef= node
    def set_nxt(self, node):
        self.nxt= node
class Deque:
    def __init__(self):
        self.front_node = self.back_node = None
        self.node_size = 0
    def push_front(self, val):
        self.node_size += 1
        if self.front_node == None:
            node = Node(val)
            self.front_node = node
            self.back_node = node
            return
        node = Node(val,nxt = self.front_node)
        self.front_node.set_bef(node)
        self.front_node = node

    def push_back(self,val):
        self.node_size += 1
        if self.back_node == None:
            node = Node(val)
            self.front_node = node
            self.back_node = node
            return
        node = Node(val,bef = self.back_node)
        self.back_node.set_nxt(node)
        self.back_node = node

    def pop_back(self):
        if self.back_node == None:
            return -1
        self.node_size -= 1
        cur = self.back_node
        self.back_node = self.back_node.get_bef()
        if self.back_node == None:
            self.front_node = None
        else:
            self.back_node.set_nxt(None)
        val = cur.get_val()
        del cur
        return val
    def pop_front(self):
        if self.front_node == None:
            return -1
        self.node_size -= 1
        cur = self.front_node
        self.front_node = self.front_node.get_nxt()
        if self.front_node == None:
            self.back_node = None
        else:
            self.front_node.set_bef(None)
        val = cur.get_val()
        del cur
        return val
    def size(self):
        return self.node_size
    def empty(self):
        if self.node_size == 0:
            return 1
        return 0
    def front(self):
        if self.front_node == None:
            return -1
        return self.front_node.get_val()
    def back(self):
        if self.back_node == None:
            return -1
        return self.back_node.get_val()
N = int(input())
deq = Deque()
result = []
for i in range(N):
    commands = list(input().split())
    func = getattr(deq,commands[0])
    if len(commands) == 1:
        result.append(func())
    else:
        func(int(commands[1]))
print('\n'.join(map(str,result)))