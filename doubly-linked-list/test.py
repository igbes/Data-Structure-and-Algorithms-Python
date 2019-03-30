import unittest
from doubly_linked_list import Node
from doubly_linked_list import LinkedList2

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
        self.list_test = LinkedList2()
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
        
        self.list_test = LinkedList2()
        self.list_test.delete(12)
        self.assertEqual(get_list_nodes(self.list_test), [])
        
        self.list_test = LinkedList2()
        self.list_test.add_in_tail(Node(12))
        self.list_test.delete(12)
        self.assertEqual(get_list_nodes(self.list_test), [])
        
        self.list_test = LinkedList2()
        self.list_test.add_in_tail(Node(12))
        self.list_test.delete(10)
        self.assertEqual(get_list_nodes(self.list_test), [12]) 
        
        self.list_test = LinkedList2()
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
        
        list_test = LinkedList2()
        self.assertEqual(list_test.find_all(12), [])
        
        list_test = LinkedList2()
        list_test.add_in_tail(Node(12))
        lst = list_test.find_all(12)
        list_value = [node.value for node in lst]        
        self.assertEqual(list_value, [12])        
        
    def test_len(self):
        
        self.assertEqual(self.list_test.len(), 6)
        
        list_test = LinkedList2()
        self.assertEqual(list_test.len(), 0)
        
    def test_insert(self):
        
        node_1000 = Node(1000)
        list_test = LinkedList2()
        list_test.insert(None, node_1000)        
        self.assertEqual(get_list_nodes(list_test), [1000])
        
        list_test = LinkedList2()
        node_12 = Node(12)
        list_test.add_in_tail(node_12)
        list_test.insert(node_12, node_1000)
        self.assertEqual(get_list_nodes(list_test), [12, 1000])
        
        list_test = LinkedList2()
        node_12 = Node(12)
        node_73 = Node(73)
        list_test.add_in_tail(node_12)
        list_test.add_in_tail(node_73)
        list_test.insert(node_12, node_1000)
        self.assertEqual(get_list_nodes(list_test), [12, 1000, 73])
        
        node_1000 = Node(1000)
        node_10 = Node(10)
        node_73 = Node(73)
        node_12 = Node(12)        
        lst = LinkedList2()
        lst.add_in_tail(node_10)
        lst.add_in_tail(node_12)
        lst.insert(node_12, node_1000)
        self.assertEqual(get_list_nodes(lst), [10, 12, 1000])
        self.assertEqual(lst.head.next.next.value, 1000)
        self.assertEqual(lst.tail.prev.value, 12)
        self.assertEqual(lst.tail.next, None)
        self.assertEqual(lst.tail.prev.next.value, 1000)
        
if __name__ == '__main__':
    unittest.main()