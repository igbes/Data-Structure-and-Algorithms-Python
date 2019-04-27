class HashTable:
    
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        
    def hash_fun(self, value):
        """Принимает в квчестве аргумента строку, возвращает индекс слота"""
        sum_code = 0
        for simbol in value:
            sum_code += ord(simbol)
        return sum_code % self.size
    
    def seek_slot(self, value):
        """Возвращает индекс пустого слота или None"""          
        slot = self.hash_fun(value)
        for i in range(0, self.size * self.step):
            if slot > self.size - 1:
                slot = slot - self.size
            if self.slots[slot] == None:
                return slot            
            slot += self.step
     
    def put(self, value):
        """Записывает значение по хэш-функции"""
        slot_number = self.seek_slot(value)
        if slot_number != None:
            self.slots[slot_number] = value
            return
        
    def find(self, value):
        """Возвращает индекс слота с искомым значением или None"""
        slot = self.hash_fun(value)
        for i in range(0, self.size * self.step):
            if slot > self.size - 1:
                slot = slot - self.size
            if self.slots[slot] == value:
                return slot            
            slot += self.step
        pass
                   
    """def show_hashtable(self):
        # Показывает хеш-таблицу в виде массива (вспомогательная функция)
        return self.slots"""