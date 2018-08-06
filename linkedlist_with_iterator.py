import unittest

class Node:
    def __init__(self, v):
        self.value = v
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current == self.tail:
            raise StopIteration
        if self.current == None:
            self.current = self.head
        else:    
            self.current = self.current.next
        return self.current.value
        
    def first(self):
        self.current = None
        
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
    def remove(self, item, boolItem = True): 
        # Удаление одного или всех узлов по значению
        # По умолчанию удаляет все узлы по значению item
        node = self.head
        preNode = Node(None)
        while node is not None:
            if node == self.head and node.value == item:
                self.head = node.next
                if boolItem == False:
                    return
            elif node.value != item:
                preNode = node
            else:
                preNode.next = node.next
                if boolItem == False:
                    return
            node = node.next
         
    #1.3    
    def clean(self):
        #Очистка списка
        self.head.value = None
        self.head.next = None
    #1.4 
    def find_all_nodes(self, item):
        # Поиск всех узлов по значению
        def iter(node, acc):
            if node is None:
                return acc
            if node.value == item:
                acc.append(node.value)
            return iter(node.next, acc)    
        return iter(self.head, [])
    # 1.5    
    def get_length(self):
        # Дать длину списка
        def iter(node, acc):
            if node is None:
                return acc
            return iter(node.next, acc + 1)
        return iter(self.head, 0)
    # 1.6
    def insert(self, item, itemIns):
        # Метод вставки узла после заданного узла
        def iter(node):
            if node is None:
                print("value missing")
                return
            if node.value == item:
                newNode = Node(itemIns)
                temp = node.next
                node.next = newNode
                newNode.next = temp
                return
            return iter(node.next)    
        return iter(self.head)
    
class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.lst = LinkedList()
        self.lst.add_in_tail(Node(12))
        self.lst.add_in_tail(Node(14))
        self.lst.add_in_tail(Node(73))
        self.lst.add_in_tail(Node(11))
        self.lst.add_in_tail(Node(77))
        self.lst.add_in_tail(Node(58)) 
    
    def tearDown(self):
        self.lst.first()
    
    def test_next(self):
        self.assertEqual(next(self.lst), 12)    
        self.assertEqual(next(self.lst), 14) 
        self.assertEqual(next(self.lst), 73) 
        self.assertEqual(next(self.lst), 11) 
        self.assertEqual(next(self.lst), 77) 
        self.assertEqual(next(self.lst), 58) 
        with self.assertRaises(StopIteration): 
            next(self.lst)
        
    def test_first(self):
        self.lst.first()
        self.assertEqual(next(self.lst), 12)    
        self.assertEqual(next(self.lst), 14) 
        self.assertEqual(next(self.lst), 73) 
        self.assertEqual(next(self.lst), 11) 
        self.assertEqual(next(self.lst), 77) 
        self.assertEqual(next(self.lst), 58) 
    
if __name__ == '__main__':
    unittest.main()
    
with self.assertRaises(StopIteration): next(self.lst)    