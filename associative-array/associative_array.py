class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        
    def hash_fun(self, key):
        """В качестве key поступают строки
        Возвращает корректный индекс слота"""
        sum_code = 0
        for simbol in key:
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
        #if key in self.slots[slot]:
        if self.is_key(key):
            index = self.slots[slot].index(key)
            self.values[slot][index] = value
        else:
            self.slots[slot].append(key)
            self.values[slot].append(value)            
            
    def get(self, key):
        """Возвращает value для key, 
        или None если ключ не найден"""
        slot = self.hash_fun(key)
        if self.slots[slot] == None:
            return None    
        if key in self.slots[slot]:
            index = self.slots[slot].index(key)
            return self.values[slot][index]
        else:
            return None