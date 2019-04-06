
class Deque:
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.insert(0,item)

    def addTail(self, item):
        self.items.append(item)
        
    def removeFront(self):
        if len(self.items) != 0:
            return self.items.pop(0)
        return None        
        
    def removeTail(self):
        if len(self.items) != 0:
            return self.items.pop()
        return None        
    
    def size(self):
        return len(self.items)        
    