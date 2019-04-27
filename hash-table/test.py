import unittest
from hash_table import HashTable

class TestHashTable(unittest.TestCase):
    
    def setUp(self):
        self.h_table = HashTable(17, 3)
        self.h_table.put("AA")
        self.h_table.put("Bc")
        self.h_table.put("dE") 
        self.h_table.put("eD")         
        
    def test_hash_fun(self):
        """Проверка работы хэш-функции"""
        self.assertEqual(self.h_table.hash_fun("dE"), 16)
        self.assertEqual(self.h_table.hash_fun("eD"), 16)
    
    def test_put(self):
        """Проверка записи значения по хэш-функции"""
        self.assertEqual(self.h_table.slots,                 
            [None, None, 'eD', None, None, None, None, None, None, None, None, 'AA', 'Bc', None, None, None, 'dE'])
       
    def test_seek_slot(self):
        """ Проверка поиска пустого слота:"""
        self.h_table = HashTable(4, 3)
        self.h_table.put("AA")
        self.h_table.put("Bc")
        self.h_table.put("dE") 
        self.h_table.put("eD")        
        self.assertEqual(self.h_table.seek_slot("DD"), None) 
        
    def test_find(self):
        """ Проверка поиска элемента по значению:"""
        self.h_table = HashTable(4, 3)
        self.h_table.put("AA")
        self.h_table.put("Bc")
        self.h_table.put("dE") 
        self.h_table.put("eD")        
        self.assertEqual(self.h_table.seek_slot("DD"), None)        
       
        self.assertEqual(self.h_table.find("dE"), 0)
        self.assertEqual(self.h_table.find("eD"), 3)
        self.assertEqual(self.h_table.find("DD"), None)
        
if __name__ == '__main__':
    unittest.main()       