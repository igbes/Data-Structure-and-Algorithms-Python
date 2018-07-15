import ctypes, unittest
class DynArray:
    
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count
    
    def make_array(self, new_capacity):
            return (new_capacity * ctypes.py_object)()
        
    def __getitem__(self,i):
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
        if self.count == self.capacity:
            self.relize(2*self.capacity)
        n = self.count
        while n > i:
            self.array[n] = self.array[n - 1]
            n = n - 1
        self.array[i] = itm 
        self.count += 1
    
    def delete(self, i):
        if self.capacity // self.count >= 2:
            self.capacity = self.count * 1.5
        n = i
        while n < self.count - 1:
            self.array[n] = self.array[n + 1]
            n = n + 1
        self.count -= 1    

    
class TestDynArray(unittest.TestCase):
    
    def setUp(self):
        self.da = DynArray()
        self.da.append(15)
        self.da.append(38)
        self.da.append(73)
        self.da.append(24)
        self.arr = []
    
    def test_insert(self):
        self.da.insert(1, 120)
        for i in range(len(self.da)):
            self.arr.append(self.da[i])        
        self.assertEqual(self.arr, [15, 120, 38, 73, 24])
        
    def test_delete(self):
        self.da.delete(1)
        for i in range(len(self.da)):
            self.arr.append(self.da[i])        
        self.assertEqual(self.arr, [15, 73, 24])        
        
        
if __name__ == '__main__':
    unittest.main()        