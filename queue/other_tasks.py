
from queue import Queue
    
def rotate_queue(q, n):
    """ "вращает" очередь по кругу на N элементов"""
    i = n
    while i > 0:
        q.enqueue(q.dequeue())
        i -= 1

class Queue_with_2stack:
    """очередь, реализованная с использованием двух стеков"""
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