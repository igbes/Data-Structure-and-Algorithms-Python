
class aBST:
    def __init__(self, depth):
        self.depth = depth
        self._length = self._get_len_array(depth)
        self.Tree = [None] * self._length
    
    def _get_len_array(self, depth_tree):
        """Возвращает количество узлов (длина списка)"""
        number_in_level = 1
        total = 1
        for level in range(depth_tree):
            number_in_level *= 2
            total += number_in_level
        return total
    
    def FindKeyIndex(self, key):
        """Поиск заданного узла по значению. Поиск ведётся от корня дерева.
        Возвращает None, если значение не найдено и достигнут предел по глубине,
        возвращает -index, если на месте предполагаемого нахождения искомого 
        елемента находится None"""
        def iter(index, level):
            if key == self.Tree[index]: 
                return index
            if level == self.depth:
                return 
            if key < self.Tree[index]:
                if self.Tree[2 * index + 1] == None:
                    return - (2 * index + 1)
                return iter(2 * index + 1, level + 1)
            else:
                if self.Tree[2 * index + 2] == None:
                    return - (2 * index + 2)
                return iter(2 * index + 2, level + 1)
        return iter(0, 0) 
    
    def AddKey(self, key):
        """Добавление узла в дерево"""
        if self.Tree[0] == None:
            self.Tree[0] = key
            return 0
        def iter(index, level):
            if level == self.depth:
                return -1           
            if key < self.Tree[index]:
                if self.Tree[2 * index + 1] == None:
                    self.Tree[2 * index + 1] = key
                    return index
                else:       
                    return iter(2 * index + 1, level + 1)
            else:
                if key > self.Tree[index]:
                    if self.Tree[2 * index + 2] == None:
                        self.Tree[2 * index + 2] = key
                        return index
                    else:       
                        return iter(2 * index + 2, level + 1)                 
        return iter(0, 0) 
    