import unittest
from dynamic_array import DynArray

class TestDynArray(unittest.TestCase):
    
    def setUp(self):
        self.da = DynArray()
        self.da.append(15)
        self.da.append(38)
        self.da.append(73)
        self.da.append(24)
        
    
    def test_insert_1(self):
        self.da.insert(1, 120)
        self.arr = []
        for i in range(len(self.da)):
            self.arr.append(self.da[i])        
        self.assertEqual(self.arr, [15, 120, 38, 73, 24])
        
    def test_insert_2(self):
        self.da.append(0)
        self.da.append(1)
        self.da.append(2)
        self.da.append(3)
        self.da.append(4)
        self.da.append(5)
        self.da.append(6)
        self.da.append(7)
        self.da.append(8)
        self.da.append(9)
        self.da.append(10)
        self.da.append(11)
        
        self.da.insert(15, 120)
        self.arr = []
        for i in range(len(self.da)):
            self.arr.append(self.da[i])        
        self.assertEqual(self.arr, [15, 38, 73, 24, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 120, 11])     
        
    def test_delete(self):
        self.da.delete(1)
        self.arr = []
        for i in range(len(self.da)):
            self.arr.append(self.da[i])        
        self.assertEqual(self.arr, [15, 73, 24])        
        
        
if __name__ == '__main__':
    unittest.main()        