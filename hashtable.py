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
    
    def seek_slot(self, value):
        slot = self.hash_fun(value)
        for i in range(slot, slot + self.step + 1):
            if self.slots[slot] == None:
                #self.slots[slot] = value
                return slot
            slot += 1
            if slot > self.size - 1:
                slot = 0
              
    def put(self, value):
        slot_number = self.seek_slot(value)
        if slot_number != None:
            self.slots[slot_number] = value
            return
        
    def find(self, value):
        slot = self.hash_fun(value)
        for i in range(slot, slot + self.step + 1):
            if self.slots[slot] == value:
                return slot
            slot += 1
            if slot > self.size - 1:
                slot = 0
        
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
                         ['eD', None, None, None, None, None, None, None, None, None, None, 'AA', 'Bc', None, None, None, 'dE'])
       
    def test_seek_slot(self):
        self.h_table = HashTable(4, 3)
        self.h_table.put("AA")
        self.h_table.put("Bc")
        self.h_table.put("dE") 
        self.h_table.put("eD")        
        self.assertEqual(self.h_table.seek_slot("DD"), None) 
        
    def test_find(self):
        self.assertEqual(self.h_table.find("dE"), 16)
        self.assertEqual(self.h_table.find("eD"), 0)
        
if __name__ == '__main__':
    unittest.main()        
    
