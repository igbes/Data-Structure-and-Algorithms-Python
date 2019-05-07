import unittest
from set import PowerSet

def show_hashtable(my_set):
    """Показывает хеш-таблицу в виде массива (вспомогательная функция для тестирования)"""
    return my_set.slots

class TestPowerSet(unittest.TestCase):
    
    def setUp(self):
        self.set_1 = PowerSet(7, 3)
        self.set_1.put("AA") 
        self.set_1.put("Bc")
        self.set_1.put("dE")
        self.set_1.put("eD")
                
        self.set_2 = PowerSet(5, 3)
        self.set_2.put("AA") 
        self.set_2.put("BB")
        self.set_2.put("dE")
        self.set_2.put("DD")
    
    def test_size(self):
        self.assertEqual(self.set_1.size(), 4)
        
    def test_remove(self):
        self.set_1.remove("Bc")
        self.assertEqual(show_hashtable(self.set_1), [None, 'dE', None, 'eD', 'AA', None, None])
      
    def test_put(self):
        self.set_1.put("Bc")
        self.set_1.put("Bc")
        self.assertEqual(show_hashtable(self.set_1), ['Bc', 'dE', None, 'eD', 'AA', None, None])
       
    def test_intersection(self):
        self.assertEqual(show_hashtable(self.set_1.intersection(self.set_2)), [None, 'dE', None, None, 'AA', None, None]) 
        
    def test_union(self):
        self.assertEqual(show_hashtable(self.set_1.union(self.set_2)), 
            ['BB', 'dE', None, None, 'eD', None, None, 'DD', None, 'Bc', 'AA', None]) 
        
    def test_difference(self):
        self.assertEqual(show_hashtable(self.set_1.difference(self.set_2)), 
            ['BB', 'eD', None, None, 'DD', None, None, None, None, 'Bc', None, None])
            
    def test_issubset(self):
        self.assertEqual(self.set_1.issubset(self.set_2), False)
        
        self.set_3 = PowerSet(5, 3)
        self.set_3.put("AA") 
        self.set_3.put("dE")
        self.assertEqual(self.set_1.issubset(self.set_3), True)       
           
if __name__ == '__main__':
    unittest.main()        

