from cache import NativeCache
import unittest

class Cache:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size
        
    def hash_fun(self, value):
        sum_code = 0
        for simbol in value:
            sum_code += ord(simbol)
        return sum_code % self.size
       
    def is_key(self, key):
        # Проверяет, имеется ли в слотах ключ
        slot = self.hash_fun(key)
        for i in range(0, self.size * self.step):
            if self.slots[slot] == None or self.slots[slot] == key:
                return slot
            slot = (slot + self.step) % self.size
        return self._get_less()
            
    def find(self, key):
        slot = self.hash_fun(key)
        for i in range(0, self.size * self.step):
            if self.slots[slot] == None:
                return                 
            if self.slots[slot] == key:
                return slot            
            slot = (slot + self.step) % self.size
            
    def put(self, key, value):
        slot_number = self.is_key(key)
        if slot_number != None:
            self.slots[slot_number] = key
            self.values[slot_number] = value
            self.hits[slot_number] += 1
        
    def _get_less(self):
        less = self.hits[0]
        index = 0
        for i in range(len(self.hits)):
            if self.hits[i] < less:
                less = self.hits[i]
                index = i
        self.hits[index] = 0        
        return index       
                   
    def show_table_keys(self):
        # Показывает массив ключей (вспомогательная функция)
        return self.slots

    def show_table_values(self):
        # Показывает массив значений (вспомогательная функция)
        return self.values
    def show_table_hits(self):
        return self.hits

class TestCache(unittest.TestCase):
    
    def setUp(self):
        self.my_cache = Cache(17, 3)
        self.my_cache.put("AA", "item 1")
        self.my_cache.put("Bc", "item 2")
        self.my_cache.put("dE", "item 3") 
        self.my_cache.put("eD", "item 4")         
        
    def test_hash_fun(self):
        self.assertEqual(self.my_cache.hash_fun("dE"), 16)
        self.assertEqual(self.my_cache.hash_fun("eD"), 16)
    
    def test_put(self):
        self.my_cache = Cache(5, 3)
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
