import unittest, random

def binary_search(ls, itm):
    
    """ Бинарный поиск """
    
    def iter(i_1, i_2, i):
        if ls[i] == itm:
            return True
        if i_1 == i_2 - 1:
            return False        
        if itm > ls[i]:
            left, right = i, i_2
        else:
            left, right = i_1, i
        return iter(left, right, (left + right) // 2)
    return iter(0, len(ls), len(ls) // 2)
    
   
class TestBinarySearch(unittest.TestCase):
           
    def setUp(self):
        self.lst = [10, 31, 53, 10, 20, 18, 45, 65, 11, 27, 22, 88, 4, 89, 67, 59, 41, 52, 30, 90, 97]
        self.l = sorted(self.lst)
        
    def test_binary_search(self):
        self.assertEqual(binary_search(self.l, 4), True)
    
    def test_binary_search(self):
        self.assertEqual(binary_search(self.l, 97), True)
        
    def test_binary_search(self):
        self.assertEqual(binary_search(self.l, 18), True)
        
    def test_binary_search(self):
        self.assertEqual(binary_search(self.l, 31), True)
        
    def test_binary_search(self):
        self.assertEqual(binary_search(self.l, 52), True) 
        
    def test_binary_search(self):
        self.assertEqual(binary_search(self.l, 50), False)
        
    def test_binary_search(self):
        self.assertEqual(binary_search(self.l, 3), False) 
        
    def test_binary_search(self):
        self.assertEqual(binary_search(self.l, 98), False)        
        
if __name__ == '__main__':
    unittest.main()          