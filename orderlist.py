import unittest

class Node2:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderList:
    # Если value = True - сортировка по возрастанию
    def __init__(self, value = True):
        self.head = None
        self.tail = None
        self.increase = value
        
    def _add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item        

    def remove(self, item):
        node = self.head
        if self.head.value == item:
            self.head = self.head.next
            self.head.prev = None
            return
        while node is not None:
            if node.value == item:
                node.prev.next = node.next
                node.next.prev = node.prev
                return
            node = node.next
            
    def _insert_in_head(self, item):
        # Вставка узла первым элементом
        newNode = Node2(item)
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        
    def is_biggest(self, itm, itm_1):
        # Сравнение элементов
        if self.increase:
            if itm >= itm_1:
                return True
            else:
                return False
        if not self.increase:
            if itm < itm_1:
                return True
            else:
                return False
            
    def insert(self, item):
        if self.head is None:
            newNode = Node2(item)
            self.head = newNode
            return
        def iter(node):
            if not self.is_biggest(item, node.value):
                self._insert_in_head(item)
                return            
            if node.next is None:
                newNode = Node2(item)
                node.next = newNode
                newNode.prev = node
                return
            if self.is_biggest(item, node.value) and not self.is_biggest(item, node.next.value):
                newNode = Node2(item)
                temp = node.next
                node.next = newNode
                newNode.prev = node
                newNode.next = temp
                temp.prev = newNode
                return        
            return iter(node.next)    
        return iter(self.head) 
    
    def find(self, item):
        node = self.head
        while self.is_biggest(item, node.value):
            if node.value == item:
                return item
            node = node.next
        return None
        
    def get_list_nodes(self, item):
    # Получить список узлов (вспомогательная функция)
        def iter(node, acc):
            if node is None:
                return acc
            acc.append(node.value)
            return iter(node.next, acc)    
        return iter(item.head, [])  

class TestOrderList(unittest.TestCase):
    def setUp(self):
        self.o_list = OrderList()
        self.o_list._add_in_tail(Node2(2))
        self.o_list._add_in_tail(Node2(3))
        self.o_list._add_in_tail(Node2(5))
        self.o_list._add_in_tail(Node2(6))       
        self.o_list._add_in_tail(Node2(7))
        
        self.o_list_1 = OrderList(False)
        self.o_list_1._add_in_tail(Node2(7))
        self.o_list_1._add_in_tail(Node2(6))
        self.o_list_1._add_in_tail(Node2(5))
        self.o_list_1._add_in_tail(Node2(3))       
        self.o_list_1._add_in_tail(Node2(2))  
        
        self.o_list_str = OrderList()
        self.o_list_str._add_in_tail(Node2("ab"))
        self.o_list_str._add_in_tail(Node2("ad"))
        self.o_list_str._add_in_tail(Node2("ae"))        
        
        self.o_list_str_1 = OrderList(False)
        self.o_list_str_1._add_in_tail(Node2("ae"))
        self.o_list_str_1._add_in_tail(Node2("ad"))
        self.o_list_str_1._add_in_tail(Node2("ab"))        
    
    # numbers
        
    def test_insert_in_middle(self):
        # Вставка узла в середину списка
        self.o_list.insert(4)
        res = self.o_list.get_list_nodes(self.o_list)
        self.assertEqual(res, [2, 3, 4, 5, 6, 7])
        
    def test_insert_in_middle_1(self):
        # Вставка узла в середину списка
        self.o_list_1.insert(4)
        res = self.o_list_1.get_list_nodes(self.o_list_1)
        self.assertEqual(res, [7, 6, 5, 4, 3, 2]) 
        
    def test_insert_in_head(self):
        # Вставка узла в начало списка
        self.o_list.insert(1)
        res = self.o_list.get_list_nodes(self.o_list)
        self.assertEqual(res, [1, 2, 3, 5, 6, 7]) 
        
    def test_insert_in_head_1(self):
        # Вставка узла в начало списка
        self.o_list_1.insert(8)
        res = self.o_list_1.get_list_nodes(self.o_list_1)
        self.assertEqual(res, [8, 7, 6, 5, 3, 2])        
          
    def test_insert_in_tail(self):
        # Вставка узла в конец списка
        self.o_list.insert(8)
        res = self.o_list.get_list_nodes(self.o_list)
        self.assertEqual(res, [2, 3, 5, 6, 7, 8])
    
    def test_insert_in_tail_1(self):
        # Вставка узла в конец списка
        self.o_list_1.insert(1)
        res = self.o_list_1.get_list_nodes(self.o_list_1)
        self.assertEqual(res, [7, 6, 5, 3, 2, 1])  
    
    def test_insert_new_node(self):
        # Создание нового списка
        self.o_list_2 = OrderList()
        self.o_list_2.insert(8)
        self.o_list_2.get_list_nodes(self.o_list_2)
        res = self.o_list_2.get_list_nodes(self.o_list_2)
        self.assertEqual(res, [8])  
        
    # strings:    
     
    def test_insert_in_middle_str(self):
        # Вставка узла в середину списка
        self.o_list_str.insert("ac")
        res = self.o_list_str.get_list_nodes(self.o_list_str)
        self.assertEqual(res, ["ab", "ac", "ad", "ae"])
    
    def test_insert_in_middle_str_1(self):
        # Вставка узла в середину списка
        self.o_list_str_1.insert("ac")
        res = self.o_list_str_1.get_list_nodes(self.o_list_str_1)
        self.assertEqual(res, ["ae", "ad", "ac", "ab"])    
        
    def test_insert_in_head_str(self):
        # Вставка узла в середину списка
        self.o_list_str.insert("aa")
        res = self.o_list_str.get_list_nodes(self.o_list_str)
        self.assertEqual(res, ["aa", "ab", "ad", "ae"])     
    
    def test_insert_in_head_str_1(self):
        # Вставка узла в середину списка
        self.o_list_str_1.insert("aa")
        res = self.o_list_str_1.get_list_nodes(self.o_list_str_1)
        self.assertEqual(res, ['ae', 'ad', 'ab', 'aa'])
    
    def test_insert_in_tail_str(self):
        # Вставка узла в середину списка
        self.o_list_str.insert("af")
        res = self.o_list_str.get_list_nodes(self.o_list_str)
        self.assertEqual(res, ["ab", "ad", "ae", "af"])
        
    def test_insert_in_tail_str_1(self):
        # Вставка узла в середину списка
        self.o_list_str_1.insert("af")
        res = self.o_list_str_1.get_list_nodes(self.o_list_str_1)
        self.assertEqual(res, ["af", "ae", "ad", "ab"])    
    
    # find
        
    def test_find(self):
        self.assertEqual(self.o_list.find(5), 5)
        
    def test_find_str(self):
        #self.o_list.find(item).value
        self.assertEqual(self.o_list_str.find("ad"), "ad")        
        
if __name__ == '__main__':
    unittest.main()        
   
