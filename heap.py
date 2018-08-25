import unittest

class Heap:
    
    def __init__(self):
        self._arr = []
        
    def add(self, item):
        """
        Вставить новый элемент
        """
        self._arr.append(item)
        if self._arr[0] == item:
            return
        i = len(self._arr) - 1
        while self._arr[(i - 1) // 2] < item:
            self._arr[(i - 1) // 2], self._arr[i] = self._arr[i], self._arr[(i - 1) // 2]
            i = (i - 1) // 2
            if i == 0:
                return            
            
    def get_heap(self):
        """
        Вернуть пирамиду в виде списка
        """
        return self._arr
            
    def del_max(self):
        """
        Удалить элемент с максимальным значением из пирамиды
        """
        self._arr[-1], self._arr[0] = self._arr[0], self._arr[-1]
        self._arr.pop()
        item = self._arr[0]
        i = 0
        while item < self._arr[i * 2 + 1] or item < self._arr[i * 2 + 2]:
            if self._arr[i * 2 + 1] > self._arr[i * 2 + 2]:
                self._arr[i], self._arr[i * 2 + 1] = self._arr[i * 2 + 1], self._arr[i]
                i = i * 2 + 1
            else:
                self._arr[i], self._arr[i * 2 + 2] = self._arr[i * 2 + 2], self._arr[i]
                i = i * 2 + 2
            if (i * 2 + 1) > len(self._arr) - 1:
                return    

class TestHeep(unittest.TestCase):
    
    def setUp(self):
        self.heap = Heap()
        self.heap.add(6)
        self.heap.add(5)
        self.heap.add(2)
        self.heap.add(1)
        self.heap.add(3)
        self.heap.add(8)
        self.heap.add(7)
        self.heap.add(4)
        self.heap.add(9)
        self.heap.add(11)
        
    def test_add(self):
        """
        Проверка вставки новых элементов
        """
        self.assertEqual(self.heap.get_heap(), [11, 9, 7, 5, 8, 2, 6, 1, 4, 3])
        
    def test_del_max(self):
        """
        Проверка удаления элемента с максимальным значением из списка
        """
        self.heap.del_max()
        self.assertEqual(self.heap.get_heap(), [9, 8, 7, 5, 3, 2, 6, 1, 4])
    
if __name__ == '__main__':
    unittest.main()      