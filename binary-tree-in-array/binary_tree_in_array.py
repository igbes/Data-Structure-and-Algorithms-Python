
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
        def iter(index, current_depth):
            if key == self.Tree[index]: 
                return index
            if current_depth == self.depth:
                return 
            if key < self.Tree[index]:
                if self.Tree[2 * index + 1] == None:
                    return - (2 * index + 1)
                return iter(2 * index + 1, current_depth + 1)
            else:
                if self.Tree[2 * index + 2] == None:
                    return - (2 * index + 2)
                return iter(2 * index + 2, current_depth + 1)
        return iter(0, 0) 
    
    def AddKey(self, key):
        def iter(index, current_depth):
            if current_depth > self.depth or self.Tree[index] == key:
                return -1
            if self.Tree[index] == None:
                self.Tree[index] = key
                return index
            if key < self.Tree[index]:
                return iter(2 * index + 1, current_depth + 1)
            if key > self.Tree[index]:
                return iter(2 * index + 2, current_depth + 1)
        return iter(0, 0)
        