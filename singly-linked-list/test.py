import unittest
from singly_linked_list import Node
from singly_linked_list import LinkedList

# Дополнительное задание 1.8
def sum_list(s1, s2):
    """Если длины списков равны, возвращает список, каждый элемент которого равен сумме соответствующих элементов входных списков."""
    if s1.len() != s2.len():
        return 
    def iter(node_1, node_2, acc):
        if node_1 is None:
            return acc
        acc.append(node_1.value + node_2.value)
        return iter(node_1.next, node_2.next, acc) 
    return iter(s1.head, s2.head, [] )

def get_list_nodes(item):
    """Вспомогательная функция для тестирования: возвращает список значений узлов (визуалицация списка)""" 
    def iter(node, acc):
        if node is None:
            return acc
        acc.append(node.value)
        return iter(node.next, acc)    
    return iter(item.head, [])   

class TestLinkedList(unittest.TestCase):
    
    def setUp(self):
        self.list_test = LinkedList()
        self.list_test.add_in_tail(Node(12))
        self.list_test.add_in_tail(Node(73))
        self.list_test.add_in_tail(Node(73))
        self.list_test.add_in_tail(Node(12))
        self.list_test.add_in_tail(Node(73))
        self.list_test.add_in_tail(Node(73))
    
    def test_delete_1(self):
        
        self.list_test.delete(12)
        self.assertEqual(get_list_nodes(self.list_test), [73, 73, 12, 73, 73])
        
    def test_delete_2(self):
        
        self.list_test.delete(12, all)
        self.assertEqual(get_list_nodes(self.list_test), [73, 73, 73, 73])
        
    def test_delete_3(self):
        
        self.list_test = LinkedList()
        self.list_test.delete(12)
        self.assertEqual(get_list_nodes(self.list_test), [])
        
        self.list_test = LinkedList()
        self.list_test.add_in_tail(Node(12))
        self.list_test.delete(12)
        self.assertEqual(get_list_nodes(self.list_test), [])
        
        self.list_test = LinkedList()
        self.list_test.add_in_tail(Node(12))
        self.list_test.delete(10)
        self.assertEqual(get_list_nodes(self.list_test), [12]) 
        
        self.list_test = LinkedList()
        self.list_test.add_in_tail(Node(11))
        self.list_test.add_in_tail(Node(12))
        self.list_test.add_in_tail(Node(73))
        self.list_test.delete(73)
        self.assertEqual(get_list_nodes(self.list_test), [11, 12])        
        
    def test_clean(self):
        
        self.list_test.clean() 
        self.assertEqual(self.list_test.head, None)
        self.assertEqual(self.list_test.tail, None)
        
    def test_find_all(self):
        
        lst = self.list_test.find_all(12)
        list_value = [node.value for node in lst]
        self.assertEqual(list_value, [12, 12]) 
        
        list_test = LinkedList()
        self.assertEqual(list_test.find_all(12), [])
        
        list_test = LinkedList()
        list_test.add_in_tail(Node(12))
        lst = list_test.find_all(12)
        list_value = [node.value for node in lst]        
        self.assertEqual(list_value, [12])        
        
    def test_len(self):
        
        self.assertEqual(self.list_test.len(), 6)
        
        list_test = LinkedList()
        self.assertEqual(list_test.len(), 0)
        
    def test_insert(self):
        
        node_1000 = Node(1000)
        list_test = LinkedList()
        list_test.insert(None, node_1000)        
        self.assertEqual(get_list_nodes(list_test), [1000])
        
        list_test = LinkedList()
        node_12 = Node(12)
        list_test.add_in_tail(node_12)
        list_test.insert(node_12, node_1000)
        self.assertEqual(get_list_nodes(list_test), [12, 1000])
        
        list_test = LinkedList()
        node_12 = Node(12)
        node_73 = Node(73)
        list_test.add_in_tail(node_12)
        list_test.add_in_tail(node_73)
        list_test.insert(node_12, node_1000)
        self.assertEqual(get_list_nodes(list_test), [12, 1000, 73])        
        
    def test_sum_list(self):
            
        list_test_1 = LinkedList()
        list_test_1.add_in_tail(Node(12))
        list_test_1.add_in_tail(Node(38))
        list_test_1.add_in_tail(Node(12))
        list_test_1.add_in_tail(Node(55))
        list_test_2 = LinkedList()
        list_test_2.add_in_tail(Node(120))
        list_test_2.add_in_tail(Node(550))
        list_test_2.add_in_tail(Node(1280))
        list_test_2.add_in_tail(Node(550))    
            
        self.assertEqual(sum_list(list_test_1, list_test_2), [132, 588, 1292, 605])
                    
        list_test_2 = LinkedList()
        list_test_2.add_in_tail(Node(120))
        list_test_2.add_in_tail(Node(550))
        list_test_2.add_in_tail(Node(1280))
               
        self.assertEqual(sum_list(list_test_1, list_test_2), None)
        
if __name__ == '__main__':
    unittest.main()