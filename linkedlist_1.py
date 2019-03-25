import unittest

class Node:
    
    def __init__(self, v):
        self.value = v
        self.next = None
        
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        
    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next
            
    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None
    
    # 1.1 - 1.2
    def delete(self, val, all=False): 
        """Удаляет один или все узлы по значению,
         по умолчанию удаляется первый нашедшийся элемент"""
        node = self.head
        preNode = Node(None)
        while node is not None:
            if node == self.head and node.value == val:
                self.head = node.next
                if all == False:
                    return
            elif node.value != val:
                preNode = node
            else:
                preNode.next = node.next
                if all == False:
                    return
            node = node.next            
         
    #1.3    
    def clean(self):
        """Очищает содержимое списка (создание пустого списка)"""
        self.head = None
        self.tail = None 
        
    #1.4 
    def find_all(self, val):
        """Возвращает список узлов по заданному значению"""
        def iter(node, acc):
            if node is None:
                return acc
            if node.value == val:
                acc.append(node)
            return iter(node.next, acc)    
        return iter(self.head, [])
    
    # 1.5    
    def len(self):
        """Возвращает длину списка"""
        def iter(node, acc):
            if node is None:
                return acc
            return iter(node.next, acc + 1)
        return iter(self.head, 0)
    
    # 1.6
    def insert(self, afterNode, newNode):
        """Вставляет узел после заданного узла по значению"""
        if self.head == None:
            self.add_in_tail(Node(newNode))
        def iter(node):
            if node is None:
                return
            if node.value == afterNode:
                new_node = Node(newNode)
                temp = node.next
                node.next = new_node
                new_node.next = temp
                return
            return iter(node.next)    
        return iter(self.head)
    
# 1.8
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
    """Вспомогательная функция: возвращает список значений узлов (визуалицация списка)""" 
    def iter(node, acc):
        if node is None:
            return acc
        acc.append(node.value)
        return iter(node.next, acc)    
    return iter(item.head, [])    

#1.7
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
        
        self.list_test.insert(73, 1000) 
        self.assertEqual(get_list_nodes(self.list_test), [12, 73, 1000, 73, 12, 73, 73])
        
        list_test = LinkedList()
        list_test.add_in_tail(Node(12))
        list_test.insert(12, 1000)
        self.assertEqual(get_list_nodes(list_test), [12, 1000])
        
        list_test = LinkedList()
        list_test.insert(None, 100)
        self.assertEqual(get_list_nodes(list_test), [100])
        
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