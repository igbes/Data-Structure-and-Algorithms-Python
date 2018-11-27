import unittest

class HashTable:
    
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        
    def hash_fun(self, value):
        sum_code = 0
        for simbol in value:
            sum_code += ord(simbol)
        return sum_code % self.size
    
    def seek_slot(self, value, find = False):
        # Режим поиска элемента по значению - find = True
        if find == False:
            slot_value = None
        else:
            slot_value = value
            
        slot = self.hash_fun(value)
        for i in range(0, self.size * self.step):
            if slot > self.size - 1:
                slot = slot - self.size
            if self.slots[slot] == slot_value:
                return slot            
            slot += self.step
     
    def put(self, value):
        slot_number = self.seek_slot(value)
        if slot_number != None:
            self.slots[slot_number] = value
            return
                   
    def show_hashtable(self):
        # Показывает хеш-таблицу в виде массива (вспомогательная функция)
        return self.slots

class TestHashTable(unittest.TestCase):
    
    def setUp(self):
        self.h_table = HashTable(17, 3)
        self.h_table.put("AA")
        self.h_table.put("Bc")
        self.h_table.put("dE") 
        self.h_table.put("eD")         
        
    def test_hash_fun(self):
        self.assertEqual(self.h_table.hash_fun("dE"), 16)
        self.assertEqual(self.h_table.hash_fun("eD"), 16)
    
    def test_put(self):
        self.assertEqual(self.h_table.show_hashtable(), 
            [None, None, 'eD', None, None, None, None, None, None, None, None, 'AA', 'Bc', None, None, None, 'dE'])
       
    def test_seek_slot(self):
        self.h_table = HashTable(4, 3)
        self.h_table.put("AA")
        self.h_table.put("Bc")
        self.h_table.put("dE") 
        self.h_table.put("eD")        
        self.assertEqual(self.h_table.seek_slot("DD"), None) 
        
        # Проверка поиска элемента по значению:
        self.assertEqual(self.h_table.seek_slot("dE", True), 0)
        self.assertEqual(self.h_table.seek_slot("eD", True), 3)
        self.assertEqual(self.h_table.seek_slot("DD", True), None)
        
if __name__ == '__main__':
    unittest.main()       
