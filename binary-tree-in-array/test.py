import unittest
from binary_tree_in_array import aBST

class TestaBST(unittest.TestCase):
    
    def setUp(self):
        """Создание дерева из 15 злементов, начиная от корня,
        глубиной, равной 3"""
        self.tree2 = aBST(3)    
        self.tree2.AddKey(50)
        self.tree2.AddKey(25)
        self.tree2.AddKey(75)
        #self.assertEqual(self.tree2.AddKey(75), 2)
        self.tree2.AddKey(37)
        self.tree2.AddKey(62)
        self.tree2.AddKey(84)
        self.tree2.AddKey(31)
        self.tree2.AddKey(43)
        self.tree2.AddKey(55)
        self.tree2.AddKey(92)
        
    # Проверка создания дерева из 15 элементов путём добавления новых узлов:
    
    def test_AddKey(self):
        self.assertEqual(self.tree2.Tree, [50, 25, 75, None, 37, 62, 84, None, None, 31, 43, 55, None, None, 92])
        
        # проверка вставки нового ключа:
        self.assertEqual(self.tree2.AddKey(23), 3)
        
        # проверка вставки уже существующего ключа:
        self.assertEqual(self.tree2.AddKey(75), 2)
        self.assertEqual(self.tree2.AddKey(84), 6)
        
        # проверка вставки ключа за пределом заданной глубины дерева:
        self.assertEqual(self.tree2.AddKey(100), -1)
        
    # Проверка поиска элемента по ключу:
        
    def test_FindKeyIndex_1(self):
        #Проверка на частично заполненном дереве
        self.assertEqual(self.tree2.FindKeyIndex(50), 0)
        self.assertEqual(self.tree2.FindKeyIndex(92), 14)
        self.assertEqual(self.tree2.FindKeyIndex(37), 4)
        self.assertEqual(self.tree2.FindKeyIndex(20), -3)
        self.assertEqual(self.tree2.FindKeyIndex(66), -12)
       
    def test_FindKeyIndex_2(self):
        #Продолжение проверки на полностью заполненном дереве (без пустых узлов)
        self.tree2.AddKey(23)
        self.tree2.AddKey(20)
        self.tree2.AddKey(24)
        self.tree2.AddKey(65)
        self.tree2.AddKey(80)
        
        self.assertEqual(self.tree2.FindKeyIndex(75), 2)
        self.assertEqual(self.tree2.FindKeyIndex(22), None) 
        self.assertEqual(self.tree2.FindKeyIndex(66), None) 
        self.assertEqual(self.tree2.FindKeyIndex(83), None)
    
if __name__ == '__main__':
    unittest.main()  
