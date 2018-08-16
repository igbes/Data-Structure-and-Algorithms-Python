import unittest

class TreeNode:
    def __init__(self, parent, value):
        self.parent = parent
        self.child = []
        self.value = value
        if parent == None:
            self.level = 0
        else:
            self.level = parent.level + 1
            
class SimpleTree:
    
    def __init__(self, root):
        self.root = root
        self.current = root
        self.node_number = 0
        self.leaf_number = 0
        self.list_node = [root.value]
        self.size = 1
        
    def add_child(self, node):
        # добавление текущему узлу нового узла в качестве дочернего
        self.current.child.append(node)
        self.size += 1
        self.list_node.append(node.value)
        
    def count_nodes(self):
        # Считает количество узлов и листьев и составляет список 
        # значений (value) узлов
        self.node_number, self.leaf_number = 0, 0
        def iter_2(node, lst):
            lst.append(node.value)
            self.node_number += 1
            if node.child != []:
                for i in node.child:
                    iter_2(i, lst)
            else:
                self.leaf_number += 1
            return lst
        return iter_2(self.root, [])
    
    def iter_tree(self, node, lst):
        # Составляет список всех узлов дерева
        lst.append(node)
        self.node_number += 1
        if node.child != []:
            for i in node.child:
                self.iter_tree(i, lst)
        else:
            self.leaf_number += 1 
        return lst
    
    def iterator(self):
        # Возвращает итератор списка узлов дерева
        return iter(self.iter_tree(self.root, []))
    
    def next_node(self, iterator):
        # Выводит узлы дерева по одному
        return next(iterator, TreeNode(None, None)).value         
        
    def find(self, item):
        # Поиск узла по значению
        list_result = []
        for node in self.iter_tree(self.root, []):
            if node.value == item:
                list_result.append(node)
        return list_result 
    
    def del_node(self, item):
        # Удаление первого в списке узла по значению, дети становятся детьми родителя
        # удаленного узла
        lst = self.find(item)
        if lst != []:
            node = lst[0]
            if node.child != []:
                for i in node.child:
                    i.parent = node.parent
                    node.parent.child.append(i)
            node.parent.child.remove(node)        
            node.child = []
            node.parent = None
            
    def move_node(self, item_1, item_2):
        # Переместить некорневой узел (item_1) дочерним узлом к другому (item_2)
        lst_1 = self.find(item_1)
        lst_2 = self.find(item_2)
        if lst_1 != []:
            for i in lst_1:
                if i == self.root:
                    continue
                else:
                    if lst_2 != []:
                        for j in lst_2:
                            i.parent.child.remove(i)
                            i.parent = j
                            j.child.append(i)
                            break

class TestSimpleTree(unittest.TestCase):
    
    def setUp(self):
        self.mtr = SimpleTree(TreeNode(None, 10))
        self.mtr.add_child(TreeNode(self.mtr.current, 5))
        self.mtr.add_child(TreeNode(self.mtr.current, 7))
        self.mtr.add_child(TreeNode(self.mtr.current, 8))
        self.mtr.current = self.mtr.current.child[0]
        self.mtr.add_child(TreeNode(self.mtr.current, 12))
        self.mtr.add_child(TreeNode(self.mtr.current, 37))
        
    def test_add_child(self):
        self.mtr.current = self.mtr.current.parent.child[1]
        self.mtr.add_child(TreeNode(self.mtr.current, 100))
        self.assertEqual(self.mtr.count_nodes(), [10, 5, 12, 37, 7, 100, 8])  
        self.assertEqual(self.mtr.node_number, 7)
        self.assertEqual(self.mtr.leaf_number, 4)
        
    def test_next_node(self):
        self.it = self.mtr.iterator()
        self.assertEqual(self.mtr.next_node(self.it), 10)    
        self.assertEqual(self.mtr.next_node(self.it), 5) 
        self.assertEqual(self.mtr.next_node(self.it), 12)
        self.assertEqual(self.mtr.next_node(self.it), 37)
        self.assertEqual(self.mtr.next_node(self.it), 7) 
        self.assertEqual(self.mtr.next_node(self.it), 8)
        self.assertEqual(self.mtr.next_node(self.it), None)
        
    def test_find(self):
        self.mtr.add_child(TreeNode(self.mtr.current, 5))
        res = []
        for i in self.mtr.find(5):
            res.append(i.value)
        self.assertEqual(res, [5, 5])
        
    def test_del_node(self): 
        self.mtr.del_node(5)
        self.assertEqual(self.mtr.count_nodes(), [10, 7, 8, 12, 37])
        
    def test_move_node(self): 
        self.mtr.move_node(5, 7)
        self.assertEqual(self.mtr.count_nodes(), [10, 7, 5, 12, 37, 8])        
            
if __name__ == '__main__':
    unittest.main()  