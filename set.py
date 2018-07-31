import unittest

class PowerSet:
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
        slot = self.hash_fun(value)
        for i in range(0, self.size * self.step):
            if slot > self.size - 1:
                slot = slot - self.size
            if self.slots[slot] == None:
                return slot            
            slot += self.step
            
    def find(self, value):
        slot = self.hash_fun(value)
        for i in range(0, self.size * self.step):
            if slot > self.size - 1:
                slot = slot - self.size
            if self.slots[slot] == None:
                return                 
            if self.slots[slot] == value:
                return slot            
            slot += self.step        
     
    def put(self, value):
        if self.find(value) == None: 
            slot_number = self.seek_slot(value)
            if slot_number != None:
                self.slots[slot_number] = value
                return slot_number
        
    def remove(self, value):
        slot = self.find(value)
        if slot != None:
            self.slots[slot] = None
           
    def intersection(self, any_set):
        new_set = PowerSet(self.size, self.step)
        for i in self.slots:
            if i == None:
                continue
            for j in any_set.slots:
                if j == None:
                    continue
                if i == j:
                    new_set.put(i)
                    break
        return new_set
    
    def union(self, any_set):
        new_set = PowerSet((self.size + any_set.size), self.step)
        for i in self.slots:
            if i == None:
                continue
            new_set.put(i)
        for j in any_set.slots:
            if j == None:
                continue
            new_set.put(j)
        return new_set       
                    
    def difference(self, any_set):
        new_set = PowerSet((self.size + any_set.size), self.step)
        union = self.union(any_set)
        intersection = self.intersection(any_set)
        for i in union.slots:
            if i == None:
                continue
            if union.find(i) != None and  not intersection.find(i) != None:
                new_set.put(i)
        return new_set        
    
    def issubset(self, any_set):
        
        for i in any_set.slots:
            if i == None:
                continue
            if self.find(i) == None:
                return False
        return True
        
    def show_hashtable(self):
        # Показывает хеш-таблицу в виде массива (вспомогательная функция)
        return self.slots


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
     
    def test_remove(self):
        self.set_1.remove("Bc")
        self.assertEqual(self.set_1.show_hashtable(), [None, 'dE', None, 'eD', 'AA', None, None])
      
  
    def test_put(self):
        self.set_1.put("Bc")
        self.set_1.put("Bc")
        self.assertEqual(self.set_1.show_hashtable(), ['Bc', 'dE', None, 'eD', 'AA', None, None])
       
     
    def test_intersection(self):
        self.assertEqual(self.set_1.intersection(self.set_2).show_hashtable(), [None, 'dE', None, None, 'AA', None, None]) 
        
       
    def test_union(self):
        self.assertEqual(self.set_1.union(self.set_2).show_hashtable(), 
            ['BB', 'dE', None, None, 'eD', None, None, 'DD', None, 'Bc', 'AA', None]) 
        

    def test_difference(self):
        self.assertEqual(self.set_1.difference(self.set_2).show_hashtable(), 
            ['BB', 'eD', None, None, 'DD', None, None, None, None, 'Bc', None, None])
            
    def test_issubset(self):
        self.assertEqual(self.set_1.issubset(self.set_2), False)
        
        self.set_3 = PowerSet(5, 3)
        self.set_3.put("AA") 
        self.set_3.put("dE")
        self.assertEqual(self.set_1.issubset(self.set_3), True)        
           
if __name__ == '__main__':
    unittest.main()        

