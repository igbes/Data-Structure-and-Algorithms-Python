import unittest

class Dict:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.values = [None] * self.size
        
    def hash_fun(self, value):
        sum_code = 0
        for simbol in value:
            sum_code += ord(simbol)
        return sum_code % self.size
       
    def is_key(self, key):
        slot = self.hash_fun(key)
        for i in range(0, self.size * self.step):
            if slot > self.size - 1:
                slot = slot - self.size
            if self.slots[slot] == None:
                return slot            
            slot += self.step 
            
    def find(self, key):
        slot = self.hash_fun(key)
        for i in range(0, self.size * self.step):
            if slot > self.size - 1:
                slot = slot - self.size
            if self.slots[slot] == None:
                return                 
            if self.slots[slot] == key:
                return slot            
            slot += self.step                
     
    def put(self, key, value):
        slot_number = self.is_key(key)
        if slot_number != None:
            self.slots[slot_number] = key
            self.values[slot_number] = value
            return
                   
    def show_table_keys(self):
        # Показывает массив ключей (вспомогательная функция)
        return self.slots

    def show_table_values(self):
        # Показывает массив значений (вспомогательная функция)
        return self.values

class TestDict(unittest.TestCase):
    
    def setUp(self):
        self.my_dict = Dict(17, 3)
        self.my_dict.put("AA", "item 1")
        self.my_dict.put("Bc", "item 2")
        self.my_dict.put("dE", "item 3") 
        self.my_dict.put("eD", "item 4")         
        
    def test_hash_fun(self):
        self.assertEqual(self.my_dict.hash_fun("dE"), 16)
        self.assertEqual(self.my_dict.hash_fun("eD"), 16)
    
    def test_put(self):
        self.assertEqual(self.my_dict.show_table_keys(), 
            [None, None, 'eD', None, None, None, None, None, None, None, None, 'AA', 'Bc', None, None, None, 'dE'])
        self.assertEqual(self.my_dict.show_table_values(), 
            [None, None, 'item 4', None, None, None, None, None, None, None, None, 'item 1', 'item 2', None, None, None, 'item 3'])        
       
    def test_is_key(self):
        # Проверка наличия свободного слота
        self.my_dict = Dict(4, 3)
        self.my_dict.put("AA", "item 1")
        self.my_dict.put("Bc", "item 2")
        self.my_dict.put("dE", "item 3") 
        self.my_dict.put("eD", "item 4")      
        self.assertEqual(self.my_dict.is_key("DD"), None) 
        
    def test_find(self):
        # Проверка поиска ключа по значению:
        self.assertEqual(self.my_dict.find("dE"), 16)
        self.assertEqual(self.my_dict.find("eD"), 2)
        self.assertEqual(self.my_dict.find("DD"), None)
        
if __name__ == '__main__':
    unittest.main()        
