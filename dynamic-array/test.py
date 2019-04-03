import unittest
from dynamic_array import DynArray

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