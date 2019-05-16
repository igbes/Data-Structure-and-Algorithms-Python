import unittest
from set import PowerSet

class TestPowerSet(unittest.TestCase):
    
    def setUp(self):
        self.set_1 = PowerSet()
        self.set_1.put("AA") 
        self.set_1.put("Bc")
        self.set_1.put("dE")
        self.set_1.put("eD")
                
        self.set_2 = PowerSet()
        self.set_2.put("AA") 
        self.set_2.put("BB")
        self.set_2.put("dE")
        self.set_2.put("DD")
    
    def test_put(self):
        self.set_1 = PowerSet()
        self.assertEqual(self.set_1.slots, 
                         [None, None, None, None, None, None, None])
        self.set_1.put("AA")
        self.set_1.put("Bc")
        self.set_1.put("dE")
        self.set_1.put("eD")
        self.assertEqual(self.set_1.slots, 
                         [None, ['dE', 'eD'], None, None, ['AA', 'Bc'], None, None])
        self.set_1.put("AA")
        self.set_1.put("Bc")
        self.set_1.put("dE")
        self.set_1.put("eD")  
        self.assertEqual(self.set_1.slots, 
                         [None, ['dE', 'eD'], None, None, ['AA', 'Bc'], None, None])
        
    def test_size(self):
        self.assertEqual(self.set_1.size(), 4)
        
    def test_remove(self):
        self.set_1.remove("Bc")
        self.assertEqual(self.set_1.slots, 
                         [None, ['dE', 'eD'], None, None, ['AA'], None, None])
      
    def test_intersection(self):
        self.assertEqual(self.set_1.intersection(self.set_2).slots, 
                         [None, ['dE'], None, None, ['AA'], None, None]) 
        
    def test_union(self):
        self.assertEqual(self.set_1.union(self.set_2).slots, 
            [None, ['dE', 'eD'], None, ['DD'], ['AA', 'Bc'], None, ['BB']])         
        
    def test_difference(self):
        self.assertEqual(self.set_1.difference(self.set_2).slots, 
            [None, ['eD'], None, None, ['Bc'], None, None])        
            
    def test_issubset(self):
        self.assertEqual(self.set_1.issubset(self.set_2), False)
        
        self.set_3 = PowerSet()
        self.set_3.put("AA") 
        self.set_3.put("dE")
        self.assertEqual(self.set_1.issubset(self.set_3), True)       
           
if __name__ == '__main__':
    unittest.main()        

