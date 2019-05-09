
class PowerSet:
    
    def __init__(self):
        self.sz = 7
        self.step = 3
        self.slots = [None] * self.sz
    
    def size(self):
        """Возвращает количество элементов в множестве"""
        res = 0
        for element in self.slots:
            if element != None:
                res += 1
        return res
        
    def hash_fun(self, value):
        """Принимает в квчестве аргумента строку, возвращает индекс слота"""
        sum_code = 0
        for simbol in value:
            sum_code += ord(simbol)
        return sum_code % self.sz
    
    def seek_slot(self, value):
        """Возвращает индекс пустого слота или None"""
        slot = self.hash_fun(value)
        for i in range(0, self.sz * self.step):
            if slot > self.sz - 1:
                slot = slot - self.sz
            if self.slots[slot] == None:
                return slot            
            slot += self.step
    
    def find(self, value):
        """Возвращает индекс слота с искомым значением или None"""
        slot = self.hash_fun(value)
        for i in range(0, self.sz * self.step):
            if slot > self.sz - 1:
                slot = slot - self.sz
            if self.slots[slot] == None:
                return                 
            if self.slots[slot] == value:
                return slot            
            slot += self.step      
    
    def put(self, value):
        """Записывает значение по хэш-функции"""
        if not self.get(value): # если value отсутствует в множестве
            slot_number = self.seek_slot(value)
            if slot_number != None: # если слот не занят из-за коллизий
                self.slots[slot_number] = value
                return slot_number
            return None
        return None
            
    def get(self, value):
        """Возвращает True если value имеется в множестве, иначе False"""
        slot = self.hash_fun(value)
        for i in range(0, self.sz * self.step):
            if slot > self.sz - 1:
                slot = slot - self.sz
            if self.slots[slot] == None:
                return False                
            if self.slots[slot] == value:
                return True                
            slot += self.step    
     
    def remove(self, value):
        """Возвращает True если value удалено"""
        slot = self.find(value)
        if slot != None:
            self.slots[slot] = None
            return True
        return False
           
    def intersection(self, set2):
        """Возвращает пересечение текущего множества и set2"""
        new_set = PowerSet()
        flag = 0
        for i in self.slots:
            if i == None:
                continue
            for j in set2.slots:
                if j == None:
                    continue
                if i == j:
                    new_set.put(i)
                    flag += 1
                    break
        if flag > 0:
            return new_set
        return None
        
    def union(self, set2):
        """Возвращает объединение текущего множества и set2"""
        new_set = PowerSet()
        new_set.sz = self.sz + set2.sz
        new_set.slots = [None] * new_set.sz
        flag = 0
        for i in self.slots:
            if i == None:
                continue
            new_set.put(i)
            flag += 1
        for j in set2.slots:
            if j == None:
                continue
            new_set.put(j)
            flag += 1
        if flag > 0:
            return new_set
        return None       
                    
    def difference(self, set2):
        """Возвращает разницу текущего множества и set2"""
        new_set = PowerSet()
        new_set.sz = self.sz + set2.sz
        new_set.slots = [None] * new_set.sz        
        union = self.union(set2)
        intersection = self.intersection(set2)
        flag = 0
        for i in union.slots:
            if i == None:
                continue
            if union.get(i) and not intersection.get(i):
                new_set.put(i)
                flag += 1
        if flag > 0:
            return new_set
        return None        
    
    def issubset(self, set2):
        """Возвращает True, если set2 есть
        подмножество текущего множества,
        иначе False"""
        for i in set2.slots:
            if i == None:
                continue
            if not self.get(i):
                return False
        return True
        
