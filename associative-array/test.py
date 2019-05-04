import unittest
from associative_array import NativeDictionary

#m_dict = NativeDictionary(17)
#print(m_dict.hash_fun('de'))
#print(m_dict.hash_fun('ed'))
#print(m_dict.slots)

class TestNativeDictionary(unittest.TestCase):
    
    def setUp(self):
        self.my_dict = NativeDictionary(17)
        self.my_dict.put("AA", "item 1")
        self.my_dict.put("Bc", "item 2")
        self.my_dict.put("dE", "item 3") 
        self.my_dict.put("eD", "item 4")         
        
    def test_hash_fun(self):
        """Проверка создания индекса слота"""
        self.assertEqual(self.my_dict.hash_fun("dE"), 16)
        self.assertEqual(self.my_dict.hash_fun("eD"), 16)
    
    def test_put(self):
        """Проверка создания пары ключ-значение"""
        self.assertEqual(self.my_dict.slots, 
            [None, None, None, None, None, None, None, None, None, None, None, ['AA'], ['Bc'], None, None, None, ['dE', 'eD']])
        self.assertEqual(self.my_dict.values, 
            [None, None, None, None, None, None, None, None, None, None, None, ['item 1'], ['item 2'], None, None, None, ['item 3', 'item 4']])
        
        self.my_dict.put("AA", "item 100")
        self.assertEqual(self.my_dict.slots, 
            [None, None, None, None, None, None, None, None, None, None, None, ['AA'], ['Bc'], None, None, None, ['dE', 'eD']])
        self.assertEqual(self.my_dict.values, 
            [None, None, None, None, None, None, None, None, None, None, None, ['item 100'], ['item 2'], None, None, None, ['item 3', 'item 4']]) 
        
        self.my_dict.put("eD", "item 200")
        self.assertEqual(self.my_dict.slots, 
            [None, None, None, None, None, None, None, None, None, None, None, ['AA'], ['Bc'], None, None, None, ['dE', 'eD']])
        self.assertEqual(self.my_dict.values, 
            [None, None, None, None, None, None, None, None, None, None, None, ['item 100'], ['item 2'], None, None, None, ['item 3', 'item 200']])         
       
    def test_is_key(self):
        """Проверка наличия ключа в слоте"""
        self.assertEqual(self.my_dict.is_key('AA'), True)
        self.assertEqual(self.my_dict.is_key('eD'), True)  
        self.assertEqual(self.my_dict.is_key('DD'), False) 
        
    def test_get(self):
        """Проверка поиска значения по ключу"""
        self.assertEqual(self.my_dict.get('dE'), 'item 3')
        self.assertEqual(self.my_dict.get("eD"), 'item 4')
        self.assertEqual(self.my_dict.get("DD"), None)
        
if __name__ == '__main__':
    unittest.main()        