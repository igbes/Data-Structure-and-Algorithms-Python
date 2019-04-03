
import ctypes

class DynArray:
    
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count
    
    def make_array(self, new_capacity):
            return (new_capacity * ctypes.py_object)()
        
    def __getitem__(self, i):
            if i < 0 or i >= self.count:
                raise IndexError('Index is out of bounds')
            return self.array[i]
        
    def resize(self, new_capacity):
            new_array = self.make_array(new_capacity)
            for i in range(self.count):
                new_array[i] = self.array[i]
            self.array = new_array
            self.capacity = new_capacity        
            
    def append(self, itm):
            if self.count == self.capacity:
                self.resize(2*self.capacity)
            self.array[self.count] = itm
            self.count += 1 
            
    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds') 
        if i == self.count:
            self.append(itm)
            return
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        n = self.count
        while n > i:
            self.array[n] = self.array[n - 1]
            n = n - 1
        self.array[i] = itm 
        self.count += 1
    
    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')        
        #if self.capacity // self.count >= 2:
        if self.count < self.capacity / 2:
            #self.capacity = self.count * 1.5
            self.capacity = int(self.capacity / 1.5)
        n = i
        while n < self.count - 1:
            self.array[n] = self.array[n + 1]
            n = n + 1
        self.count -= 1    
