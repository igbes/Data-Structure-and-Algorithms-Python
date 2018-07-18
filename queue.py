import unittest
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def first(self):
        return self.items[-1]
    
class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def push(self, value):
        return self.stack.append(value)

    def peak(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)    
    
class Queue_1:
    # очередь, реализованная с использованием стеков
    def __init__(self):
        self.st_1 = Stack()
        self.st_2 = Stack()

    def enqueue(self, item):
        self.st_1.push(item)
    def dequeue(self):
        i = self.st_1.size()
        while i > 0:
            self.st_2.push(self.st_1.pop())
            i -= 1
        res = self.st_2.pop()
        i = self.st_2.size()
        while i > 0:
            self.st_1.push(self.st_2.pop())
            i -= 1
        return res    
    def size(self):
        return self.st_1.size()
    
    def first(self):
        i = self.st_1.size()
        while i > 0:
            self.st_2.push(self.st_1.pop())
            i -= 1
        res = self.st_2.peak()
        i = self.st_2.size()
        while i > 0:
            self.st_1.push(self.st_2.pop())
            i -= 1
        return res    
    
def rotate_queue(q, n):
    i = n
    while i > 0:
        q.enqueue(q.dequeue())
        i -= 1
    return q.first()  


class TestQueue(unittest.TestCase):
    
    def setUp(self):
        self.qu = Queue()
        self.qu_1 = Queue_1()
        self.qu.enqueue(1)
        self.qu.enqueue(2)
        self.qu.enqueue(3)
        self.qu.enqueue(4)
        self.qu.enqueue(5)        
        self.qu_1.enqueue(1)
        self.qu_1.enqueue(2)
        self.qu_1.enqueue(3)
        self.qu_1.enqueue(4)
        self.qu_1.enqueue(5) 
        
    def test_rotate_queue(self):
        self.assertEqual(rotate_queue(self.qu, 3), 4)
        self.assertEqual(rotate_queue(self.qu_1, 3), 4)
           
if __name__ == '__main__':
    unittest.main()        