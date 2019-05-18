from cache import NativeCache
import unittest

class TestCache(unittest.TestCase):
    
    def setUp(self):
        self.my_cache = NativeCache(17, 3)
        self.my_cache.put("AA", "item 1")
        self.my_cache.put("Bc", "item 2")
        self.my_cache.put("dE", "item 3") 
        self.my_cache.put("eD", "item 4")         
        
    def test_hash_fun(self):
        self.assertEqual(self.my_cache.hash_fun("dE"), 16)
        self.assertEqual(self.my_cache.hash_fun("eD"), 16)
    
    def test_put(self):
        self.my_cache = NativeCache(5, 3)
        self.my_cache.put("AA", "item 1")
        self.my_cache.put("Bc", "item 2")
        self.my_cache.put("dE", "item 3") 
        self.my_cache.put("eD", "item 4") 
        self.assertEqual(self.my_cache.show_table_keys(), ['AA', None, 'eD', 'Bc', 'dE'])
        self.assertEqual(self.my_cache.show_table_values(), ['item 1', None, 'item 4', 'item 2', 'item 3']) 
        self.my_cache.put("Bc", "item 5")
        self.assertEqual(self.my_cache.show_table_keys(), ['AA', None, 'eD', 'Bc', 'dE'])
        self.assertEqual(self.my_cache.show_table_values(), ['item 1', None, 'item 4', 'item 5', 'item 3'])
        self.assertEqual(self.my_cache.show_table_hits(), [1, 0, 1, 2, 1])
        self.my_cache.put("AA", "item 7")
        self.my_cache.put("AA", "item 7")
        self.my_cache.put("BB", "item 9")
        # Проверка удаления наименее часто используемого элемента при отсутствии места в хеш-таблице,
        # удаляется первый наименьший элемент и вставляется новый
        self.assertEqual(self.my_cache.show_table_hits(), [3, 1, 1, 2, 1])
        self.my_cache.put("TT", "item 100")
        self.assertEqual(self.my_cache.show_table_keys(), ['AA', 'TT', 'eD', 'Bc', 'dE'])
        self.assertEqual(self.my_cache.show_table_values(), ['item 7', 'item 100', 'item 4', 'item 5', 'item 3'])
        self.assertEqual(self.my_cache.show_table_hits(), [3, 1, 1, 2, 1])

    def test_find(self):
        # Проверка поиска ключа по значению:
        self.assertEqual(self.my_cache.find("dE"), 16)
        self.assertEqual(self.my_cache.find("eD"), 2)
        self.assertEqual(self.my_cache.find("DD"), None)
        
if __name__ == '__main__':
    unittest.main()       
