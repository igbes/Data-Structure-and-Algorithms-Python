import unittest

class Stack:
    def __init__(self):
        self.stack = []
   
    def size(self):
        return len(self.stack)    
        
    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop()
        return None
        

    def push(self, value):
        self.stack.append(value)
        return value
        
    def peak(self):
        if len(self.stack) != 0:
            return self.stack[-1]
        return None
        

    