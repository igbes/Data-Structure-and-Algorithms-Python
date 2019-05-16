
class PowerSet:
    
    def __init__(self):
        self.sz = 7
        self.step = 3
        self.slots = [None] * self.sz
    
    def size(self):
        """Возвращает количество элементов в множестве"""
        arr = self.flatten(self.slots)
        return len(arr)
    
    def put(self, value):
        """аписывает значение по хэш-функции"""
        slot = self.hash_fun(value)
        if self.slots[slot] is None:
            self.slots[slot] = []
            self.slots[slot].append(value)
        else:
            if value in self.slots[slot]:
                return
            self.slots[slot].append(value)
        return slot    
    
    def get(self, value):
        """Возвращает True если value имеется в множестве, иначе False"""
        slot = self.hash_fun(value)
        if self.slots[slot] is not None:
            if value in self.slots[slot]:
                return True
            return False
        return False
    
    def remove(self, value):
        """Возвращает True если value удалено"""
        slot = self.hash_fun(value)
        if self.slots[slot] is not None:
            if value in self.slots[slot]:
                self.slots[slot].remove(value)
                return True
            return False
        return False
        
    def intersection(self, set2):
        """Возвращает пересечение текущего множества и set2"""
        res = PowerSet()
        #res = []
        flag = 0
        arr_set1 = self.flatten(self.slots)
        arr_set2 = self.flatten(set2.slots)
        for element_1 in arr_set1:
            for element_2 in arr_set2:
                if element_1 == element_2:
                    #res.append(element_1)
                    res.put(element_1)
                    flag += 1
        if flag > 0:            
            return res            
        return None    
        
    def union(self, set2):
        """Возвращает объединение текущего множества и set2"""
        res_set = PowerSet()
        res = []
        flag = 0
        arr_set1 = self.flatten(self.slots)
        arr_set2 = self.flatten(set2.slots)      
        for element in arr_set1:
            if not element in arr_set2:
                res.append(element)
                flag += 1
        if flag > 0:
            for elem in arr_set2 + res:
                res_set.put(elem)
            return res_set
        return None
    
    def difference(self, set2):
        """Возвращает разницу текущего множества и set2"""
        res_set = PowerSet()
        res = []
        flag = 0
        arr_set1 = self.flatten(self.slots)
        arr_set2 = self.flatten(set2.slots)         
        for element in arr_set1:
            if not element in arr_set2:
                res_set.put(element)
                flag += 1
        if flag > 0:
            return res_set
        return None
    
    def issubset(self, set2):
        """Возвращает True, если set2 есть
        подмножество текущего множества,
        иначе False"""
        arr_set1 = self.flatten(self.slots)
        arr_set2 = self.flatten(set2.slots)         
        for element in arr_set2:
            if not element in arr_set1:
                return False
        return True    
            
    def hash_fun(self, value):
        """Принимает в квчестве аргумента строку, возвращает индекс слота"""
        sum_code = 0
        for simbol in value:
            sum_code += ord(simbol)
        return sum_code % self.sz
    
    def flatten(self, arr):
        res = []
        for elem in arr:
            if elem != None:
                for i in elem:
                    res.append(i)
        return res