
class NativeCache:
    
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size
        
    def hash_fun(self, value):
        """Возвращает корректный индекс слота"""
        sum_code = 0
        for simbol in value:
            sum_code += ord(simbol)
        return sum_code % self.size
       
    def is_key(self, key):
        """Возвращает True, если ключ имеется, иначе False"""
        slot = self.hash_fun(key)
        if self.slots[slot] == None:
            return False
        if key in self.slots[slot]:
            return True
        return False
    
    def put(self, key, value):
        """Гарантированно записывает заначение value по ключу key"""
        slot = self.hash_fun(key)
        if self.slots[slot] == None:
            self.slots[slot] = []
            self.values[slot] = []
            self.hits[slot] = []
        if self.is_key(key):
            index = self.slots[slot].index(key)
            self.values[slot][index] = value
            self.hits[slot][index] += 1
        else:
            if len(self.slots[slot]) == 2:
                min_value = min(self.hits[slot])
                index = self.hits[slot].index(min_value)
                self.hits[slot].remove(self.hits[slot][index])
                self.values[slot].remove(self.values[slot][index])
                self.slots[slot].remove(self.slots[slot][index])
            self.slots[slot].append(key)
            self.values[slot].append(value)  
            self.hits[slot].append(1)
    
    def get(self, key):
        """Возвращает value для key, 
        или None если ключ не найден"""
        slot = self.hash_fun(key)
        if self.slots[slot] == None:
            return None    
        if key in self.slots[slot]:
            index = self.slots[slot].index(key)
            self.hits[slot][index] += 1
            return self.values[slot][index]
        else:
            return None
        
    