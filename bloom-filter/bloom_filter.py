class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = [0] * f_len
        
    def hash1(self, str1):
        # 17
        random_number = 17
        sum = 0
        for c in str1:
            code = ord(c)
            sum = (sum * random_number + code)
        return sum % self.filter_len   
        # реализация ...

    def hash2(self, str1):
        # 223 
        random_number = 223
        sum = 0
        for c in str1:
            code = ord(c)
            sum = (sum * random_number + code)
        return sum % self.filter_len       
       
    def add(self, str1):
        """добавляем строку str1 в фильтр"""
        self.filter[self.hash1(str1)] = 1
        self.filter[self.hash2(str1)] = 1
        
    def is_value(self, str1):
        """проверка, имеется ли строка str1 в фильтре"""
        if self.filter[self.hash1(str1)] and self.filter[self.hash2(str1)]:
            return True
        return False
        