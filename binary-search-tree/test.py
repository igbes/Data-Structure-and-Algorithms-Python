import unittest
from binary_search_tree import BST
from binary_search_tree import BSTFind
from binary_search_tree import BSTNode

class TestBST(unittest.TestCase):
    
    def setUp(self):
        # Создание дерева из 15 злементов начиная от корня (8)
        self.tree = BST(BSTNode(8, 80, None))
        self.tree.AddKeyValue(4, 40)
        self.tree.AddKeyValue(12, 120)
        self.tree.AddKeyValue(2, 20)
        self.tree.AddKeyValue(6, 60) 
        self.tree.AddKeyValue(10, 100)
        self.tree.AddKeyValue(14, 140)
        self.tree.AddKeyValue(1, 10)
        self.tree.AddKeyValue(3, 30)
        self.tree.AddKeyValue(5, 50)
        self.tree.AddKeyValue(7, 70)
        self.tree.AddKeyValue(9, 90)
        self.tree.AddKeyValue(11, 110)
        self.tree.AddKeyValue(13, 130)
        self.tree.AddKeyValue(15, 150)
        
    def test_AddKeyValue(self):
        # проверка добавления элементов и создания дерево из 15 узлов
        self.assertEqual([node.NodeKey for node in self.tree.GetNodeList()], [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15]) 
        self.tree.AddKeyValue(12, 120)
        self.assertEqual([node.NodeKey for node in self.tree.GetNodeList()], [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15]) 
        
    def test_FindNodeByKey(self):
        # Проверка поиска элемента по ключу
        self.assertEqual(self.tree.FindNodeByKey(12).NodeHasKey, True)
        self.assertEqual(self.tree.FindNodeByKey(10).NodeHasKey, True)
        self.assertEqual(self.tree.FindNodeByKey(25).NodeHasKey, False)
        self.assertEqual(self.tree.FindNodeByKey(0).NodeHasKey, False)
        
        
    def test_FinMinMax(self):
        # Проверка нахождения максимального или минимального значения
        self.assertEqual(self.tree.FinMinMax(self.tree.Root, True).NodeKey, 15)
        self.assertEqual(self.tree.FinMinMax(self.tree.Root, False).NodeKey, 1)
        self.assertEqual(self.tree.FinMinMax(self.tree.Root.RightChild, True).NodeKey, 15)        
        self.assertEqual(self.tree.FinMinMax(self.tree.Root.RightChild.LeftChild, False).NodeKey, 9)
        #self.assertEqual(self.tree.FinMinMax(9).key, 9)
    
        # Проверка удаления элемента:
    
    def test_DeleteNodeByKey_1(self): 
        self.assertEqual([node.NodeKey for node in self.tree.GetNodeList()], [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15]) 
        self.tree.DeleteNodeByKey(12)
        self.assertEqual([node.NodeKey for node in self.tree.GetNodeList()], [8, 4, 2, 1, 3, 6, 5, 7, 13, 10, 9, 11, 14, 15])
        
    def test_DeleteNodeByKey_2(self): 
        self.assertEqual([node.NodeKey for node in self.tree.GetNodeList()], [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15]) 
        self.tree.DeleteNodeByKey(14)
        self.assertEqual([node.NodeKey for node in self.tree.GetNodeList()], [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 15, 13])
        
    def test_DeleteNodeByKey_3(self): 
        self.assertEqual([node.NodeKey for node in self.tree.GetNodeList()], [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15])
        self.tree.DeleteNodeByKey(2)
        self.assertEqual([node.NodeKey for node in self.tree.GetNodeList()], [8, 4, 3, 1, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15])
         
    def test_DeleteNodeByKey_4(self): 
        self.assertEqual([node.NodeKey for node in self.tree.GetNodeList()], [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15])
        self.tree.DeleteNodeByKey(1)
        self.assertEqual([node.NodeKey for node in self.tree.GetNodeList()], [8, 4, 2, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15])
        
    def test_Count(self):
        # проверка подсчёта количества узлов дерева
        self.assertEqual(self.tree.Count(), 15)
        self.tree = BST(BSTNode(8, 80, None))
        self.assertEqual(self.tree.Count(), 1)
        
    # проверка обходов дерева в глубину ------------------------------------------
        
    def test_DeepAllNodes(self):
        # проверка in-order
        self.assertEqual([node.NodeKey for node in list(self.tree.DeepAllNodes(0))], 
                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.tree = BST(BSTNode(8, 80, None))
        self.assertEqual([node.NodeKey for node in list(self.tree.DeepAllNodes(0))], [8]) 
        
    def test_DeepAllNodes(self):
        # проверка post-order
        self.assertEqual([node.NodeKey for node in list(self.tree.DeepAllNodes(1))], 
                         [1, 3, 2, 5, 7, 6, 4, 9, 11, 10, 13, 15, 14, 12, 8])
        self.tree = BST(BSTNode(8, 80, None))
        self.assertEqual([node.NodeKey for node in list(self.tree.DeepAllNodes(0))], [8])        
                         
    def test_DeepAllNodes(self):
        # проверка pre-order
        self.assertEqual([node.NodeKey for node in list(self.tree.DeepAllNodes(2))], 
                         [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15]) 
        self.tree = BST(BSTNode(8, 80, None))
        self.assertEqual([node.NodeKey for node in list(self.tree.DeepAllNodes(0))], [8])        
    
    # проверка обхода дерева в ширину --------------------------------------------
                         
    def test_WideAllNodes(self):
        self.assertEqual([node.NodeKey for node in list(self.tree.WideAllNodes())], 
                         [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])
        self.tree = BST(BSTNode(8, 80, None))
        self.assertEqual([node.NodeKey for node in list(self.tree.DeepAllNodes(0))], [8])        
        
if __name__ == '__main__':
    unittest.main()  