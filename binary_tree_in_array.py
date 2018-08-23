import unittest

class Tree2inArray:
    def __init__(self, depth):
        self.depth = depth
        self._length = self._get_len_array(depth)
        self._arr = [None for lst in range(self._length)]
    
    def _get_len_array(self, depth_tree):
        """
        Возвращает количество узлов (длина списка)
        """
        number_in_level = 1
        total = 1
        for level in range(depth_tree):
            number_in_level *= 2
            total += number_in_level
        return total
    
    def get_tree(self):
        """
        Возвращает список узлов (дерево в массиве)
        """
        return self._arr
    
    def find(self, item):
        """
        Поиск заданного узла по значению. Поиск ведётся от корня дерева.
        Возвращает None, если значение не найдено и достигнут предел по глубине,
        возвращает -index, если на месте предполагаемого нахождения искомого 
        елемента находится None
        """
        def iter(index, level):
            if item == self._arr[index]: 
                return index
            if level == self.depth:
                return
            if item < self._arr[index]:
                if self._arr[2 * index + 1] == None:
                    return - (2 * index + 1)
                return iter(2 * index + 1, level + 1)
            else:
                if self._arr[2 * index + 2] == None:
                    return - (2 * index + 2)
                return iter(2 * index + 2, level + 1)
        return iter(0, 0) 
    
    def add(self, item):
        """
        Добавление узла в дерево
        """
        if self._arr[0] == None:
            self._arr[0] = item
            return
        def iter(index, level):
            if level == self.depth:
                return            
            if item < self._arr[index]:
                if self._arr[2 * index + 1] == None:
                    self._arr[2 * index + 1] = item
                    return 
                else:       
                    return iter(2 * index + 1, level + 1)
            else:
                if item > self._arr[index]:
                    if self._arr[2 * index + 2] == None:
                        self._arr[2 * index + 2] = item
                        return 
                    else:       
                        return iter(2 * index + 2, level + 1)                 
        return iter(0, 0) 
    
class TestTree2inArray(unittest.TestCase):
    
    def setUp(self):
        """
        Создание дерева из 15 злементов, начиная от корня,
        глубиной, равной 3 
        """
        self.tree2 = Tree2inArray(3)    
        self.tree2.add(50)
        self.tree2.add(25)
        self.tree2.add(75)
        self.tree2.add(37)
        self.tree2.add(62)
        self.tree2.add(84)
        self.tree2.add(31)
        self.tree2.add(43)
        self.tree2.add(55)
        self.tree2.add(92)          
        
    def test_add(self):
        """
        Проверка создания дерева из 15 элементов путём добавления новых узлов
        """
        self.assertEqual(self.tree2.get_tree(), [50, 25, 75, None, 37, 62, 84, None, None, 31, 43, 55, None, None, 92])  
    
        # Проверка поиска элемента по ключу:
        
    def test_find_1(self):
        """
        Проверка на частично заполненном дереве
        """
        self.assertEqual(self.tree2.find(50), 0)
        self.assertEqual(self.tree2.find(92), 14)
        self.assertEqual(self.tree2.find(37), 4)
        self.assertEqual(self.tree2.find(20), -3)
        self.assertEqual(self.tree2.find(66), -12)
       
    def test_find_2(self):
        """
        Продолжение проверки на полностью заполненном дереве
        (без пустых узлов)
        """
        self.tree2.add(23)
        self.tree2.add(20)
        self.tree2.add(21)
        self.tree2.add(65)
        self.tree2.add(80)
        
        self.assertEqual(self.tree2.find(75), 2)
        self.assertEqual(self.tree2.find(22), None) 
        self.assertEqual(self.tree2.find(66), None) 
        self.assertEqual(self.tree2.find(83), None) 
    
if __name__ == '__main__':
    unittest.main()  
