import unittest

class Tree2Node:
    def __init__(self, key):
        self.parent = None
        self.left = None
        self.right = None
        self.key = key
        
class Tree2:
    def __init__(self):
        self.root = None
           
    def add(self, item):
        """
        Добавление узла в дерево
        """
        new_node = Tree2Node(item)
        if not self.root:
            self.root = new_node
            self.current = new_node
            return
        def iter(node):
            if new_node.key < node.key:
                if not node.left:
                    node.left = new_node
                    new_node.parent = node
                    return 
                else:       
                    return iter(node.left)
            else:
                if not node.right:
                    node.right = new_node
                    new_node.parent = node
                    return 
                else:       
                    return iter(node.right)                 
        return iter(self.root) 
    
    def count_nodes(self):
        """
        Составляет список ключей (key) узлов
        """
        def iter(node, lst):
            lst.append(node.key)
            if node.left:
                iter(node.left, lst)
            if node.right:
                iter(node.right, lst)
            return lst
        return iter(self.root, [])
    
    def find(self, item):
        """
        Поиск заданного узла по значению. Поиск ведётся от корня дерева.
        """
        def iter(node):
            if item == node.key:
                return node            
            if item < node.key:
                if not node.left:
                    return
                return iter(node.left)
            else:
                if not node.right:
                    return
                return iter(node.right)
        return iter(self.root)
    
    def find_extremum(self, item, f = 1):
        """
        Поиск максимального или минимального значения относительно заданного узла,
        узел задаётся значением ключа item; по умолчанию f = 1 - ищется максимум, 
        иначе - минимум
        """
        find_node = self.find(item)
        if not find_node:
            return
        def iter(node):
            if f == 1:
                if not node.right:
                    return node
                return iter(node.right)
            else:
                if not node.left:
                    return node
                return iter(node.left)
        return iter(find_node) 
    
    def del_node(self, item):
        """
        Удаление заданного узла по значению
        """
        del_node = self.find(item)
        if not del_node:
            return
        if not del_node.left and not del_node.right:
            if del_node.parent.left == del_node:
                del_node.parent.left = None
            else:
                del_node.parent.right = None
            del_node.parent = None
            return                
        def iter(node):
            if not node.left and not node.right:
                if node.parent.left == node:
                    node.parent.left = None
                else:
                    node.parent.right == None
                node.parent = del_node.parent
                if del_node.parent.left == del_node:
                    del_node.parent.left = node
                else:
                    del_node.parent.right = node
                if del_node.left != node:
                    node.left = del_node.left
                else:
                    node.left = None
                if del_node.right != node:
                    node.right = del_node.right
                else:
                    node.right = None
                del_node.parent = None
                del_node.left = None
                del_node.right = None
                return
            if node.left:    
                return iter(node.left)
            else:
                return iter(node.right)
        return iter(del_node.right)          
    
class TestTree2(unittest.TestCase):
    
    def setUp(self):
        # Создание дерева из 15 злементов начиная от корня (8)
        self.tree = Tree2()
        self.tree.add(8)
        self.tree.add(4)
        self.tree.add(12)
        self.tree.add(2)
        self.tree.add(6) 
        self.tree.add(10)
        self.tree.add(14)
        self.tree.add(1)
        self.tree.add(3)
        self.tree.add(5)
        self.tree.add(7)
        self.tree.add(9)
        self.tree.add(11)
        self.tree.add(13)
        self.tree.add(15)  
        
    def test_add(self):
        # Проверка создания дерева из 15 элементов путём добавления новых узлов
        self.assertEqual(self.tree.count_nodes(), [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15])  
        
    def test_tree_find(self):
        # Проверка поиска элемента по ключу
        self.assertEqual(self.tree.find(12).key, 12)
        self.assertEqual(self.tree.find(25), None)
        
    def test_find_extremum(self):
        # Проверка нахождения максимального или минимального значения
        self.assertEqual(self.tree.find_extremum(12).key, 15)        
        self.assertEqual(self.tree.find_extremum(6, 0).key, 5)
        self.assertEqual(self.tree.find_extremum(9).key, 9)
    
        # Проверка удаления элемента:
    
    def test_del_node_1(self): 
        self.tree.del_node(12)
        self.assertEqual(self.tree.count_nodes(), [8, 4, 2, 1, 3, 6, 5, 7, 13, 10, 9, 11, 14, 15])
        
    def test_del_node_2(self): 
        self.tree.del_node(14)
        self.assertEqual(self.tree.count_nodes(), [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 15, 13])
        
    def test_del_node_3(self): 
        self.tree.del_node(2)
        self.assertEqual(self.tree.count_nodes(), [8, 4, 3, 1, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15])
         
    def test_del_node_4(self): 
        self.tree.del_node(1)
        self.assertEqual(self.tree.count_nodes(), [8, 4, 2, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15])
        
if __name__ == '__main__':
    unittest.main()  
    