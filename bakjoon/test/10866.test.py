import sys
input = sys.stdin.readline

from collections import deque
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
        val = cur.get_val()
        self.back_node = self.back_node.get_bef()
        if self.back_node == None:
            self.front_node = None
        else:
            self.back_node.set_nxt(None)
        
        del cur
        return val
    def pop_front(self):
        if self.front_node == None:
            return -1
        self.node_size -= 1
        cur = self.front_node
        val = cur.get_val()
        self.front_node = self.front_node.get_nxt()
        if self.front_node == None:
            self.back_node = None
        else:
            self.front_node.set_bef(None)
        
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
    def print(self):
        cur = self.front_node
        result = []
        while cur!= None:
            result.append(cur.get_val())
            cur = cur.get_nxt()
        print(*result)
deq = Deque()
original_deq = deque()
result = [-90]
ori_result = [-90]

commands_all = ['push_front', 'push_back', 'pop_front', 'pop_back','size', 'empty','front', 'back']
import random
while True:
    commands = [random.choice(commands_all)]
    if commands[0] == 'push_back' or commands[0] == 'push_front':
        commands.append(random.randint(1,10000))
    func = getattr(deq,commands[0])
    print(*commands)
    if len(commands) == 1:
        result.append(func())
    else:
        func(int(commands[1]))
    
    if commands[0] == 'push_back':
        original_deq.append(commands[1])
    elif commands[0] == 'push_front':
        original_deq.appendleft(commands[1])
    elif commands[0] == 'pop_front':
        try:
            ori_result.append(original_deq.popleft())
        except:
            ori_result.append(-1)
    elif commands[0] == 'pop_back':
        try:
            ori_result.append(original_deq.pop())
        except:
            ori_result.append(-1)
    elif commands[0] == 'size':
        ori_result.append(len(original_deq))
    elif commands[0] == 'empty':
        ori_result.append(int(len(original_deq)==0))
    elif commands[0] == 'front':
        try:
            ori_result.append(original_deq[0])
        except:
            ori_result.append(-1)
        
    elif commands[0] == 'back':
        try:
            ori_result.append(original_deq[-1])
        except:
            ori_result.append(-1)
    deq.print()
    print(*original_deq)
    if int(result[-1]) != int(ori_result[-1]):
        print(result, ori_result)
        break
    # deq.print()
print('\n'.join(map(str,result)))