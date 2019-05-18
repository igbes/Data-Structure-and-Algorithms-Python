class NativeCache:
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