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
    # 1.1
    def remove(self, item): 
        # Удаление одного узла по значению
        node = self.head
        if self.head.value == item:
            self.head = self.head.next
            return
        while node is not None:
            if node.next == None:
                return #print("value is missing")
            if node.next.value == item:
                node.next = node.next.next
                return
            node = node.next 
    # 1.2        
    def remove_all_value(self, item):
        # Удаление всех узлов по значению
        node = self.head
        if self.head.value == item:
            self.head = self.head.next
        while node is not None:
            if node.next == None:
                return 
            if node.next.value == item:
                node.next = node.next.next
                #return
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
    
# 1.7
def sum_s_list(s1, s2):
    if s1.get_length() != s2.get_length():
        return print("lists of different lengths")
    def iter(node_1, node_2, acc):
        if node_1 is None:
            return acc
        acc.append(node_1.value + node_2.value)
        return iter(node_1.next, node_2.next, acc) 
    return iter(s1.head, s2.head, [] )

def get_list_nodes(item):
    # Получить список узлов (вспомогательная функция)
    def iter(node, acc):
        if node is None:
            return acc
        acc.append(node.value)
        return iter(node.next, acc)    
    return iter(item.head, [])    

def test_remove():
    s_list_test_1 = LinkedList()
    s_list_test_1.add_in_tail(Node(12))
    s_list_test_1.add_in_tail(Node(38))
    s_list_test_1.add_in_tail(Node(12))
    s_list_test_1.add_in_tail(Node(55))
    s_list_test_1.remove(12)
    if get_list_nodes(s_list_test_1) == [38, 12, 55]:
        print("test remove(item) is OK")
    else:
        print("test remove(item) is FAIL")
   
def test_remove_all_value():
    s_list_test_2 = LinkedList()
    s_list_test_2.add_in_tail(Node(12))
    s_list_test_2.add_in_tail(Node(38))
    s_list_test_2.add_in_tail(Node(12))
    s_list_test_2.add_in_tail(Node(55))
    s_list_test_2.remove_all_value(12)
    if get_list_nodes(s_list_test_2) == [38, 55]:
        print("test_remove_all_value(item) is OK")
    else:    
        print("test_remove_all_value(item) is FAIL")
    
def test_clean():
    s_list_test_3 = LinkedList()
    s_list_test_3.add_in_tail(Node(12))
    s_list_test_3.add_in_tail(Node(38))
    s_list_test_3.add_in_tail(Node(12))
    s_list_test_3.add_in_tail(Node(55))
    s_list_test_3.clean()
    if get_list_nodes(s_list_test_3) == [None]:
        print("test_clean() is OK")
    else:    
        print("test_clean() is FAIL")

def test_find_all_nodes():
    s_list_test_4 = LinkedList()
    s_list_test_4.add_in_tail(Node(12))
    s_list_test_4.add_in_tail(Node(38))
    s_list_test_4.add_in_tail(Node(12))
    s_list_test_4.add_in_tail(Node(55))
    if s_list_test_4.find_all_nodes(12) == [12, 12]:
        print("test find_all_nodes(item) is OK")
    else:
        print("test find_all_nodes(item) is FAIL")

def test_get_length():
    s_list_test_5 = LinkedList()
    s_list_test_5.add_in_tail(Node(12))
    s_list_test_5.add_in_tail(Node(38))
    s_list_test_5.add_in_tail(Node(12))
    s_list_test_5.add_in_tail(Node(55))
    
    if s_list_test_5.get_length() == 4:
        print("test get_length(item) is OK")
    else:
        print("test get_length(item) is FAIL")

def test_insert():
    s_list_test_6 = LinkedList()
    s_list_test_6.add_in_tail(Node(12))
    s_list_test_6.add_in_tail(Node(38))
    s_list_test_6.add_in_tail(Node(12))
    s_list_test_6.add_in_tail(Node(55))
    s_list_test_6.insert(38, 73)
    if get_list_nodes(s_list_test_6) == [12, 38, 73, 12, 55]:
        print("test insert(item_1, item_2) is OK")
    else:
        print("test remove(item_1, item_2) is FAIL")
        
def test_sum_s_list():
    s_list_test_7 = LinkedList()
    s_list_test_7.add_in_tail(Node(12))
    s_list_test_7.add_in_tail(Node(38))
    s_list_test_7.add_in_tail(Node(12))
    s_list_test_7.add_in_tail(Node(55))
    s_list_test_8 = LinkedList()
    s_list_test_8.add_in_tail(Node(120))
    s_list_test_8.add_in_tail(Node(550))
    s_list_test_8.add_in_tail(Node(1280))
    s_list_test_8.add_in_tail(Node(550))    
    
    if sum_s_list(s_list_test_7, s_list_test_8) == [132, 588, 1292, 605]:
        print("test sum_s_list(item_1, item_2) is OK")
    else:
        print("test sum_s_list(item_1, item_2) is FAIL")

test_remove()
test_remove_all_value()  
test_clean()
test_find_all_nodes()
test_get_length()
test_insert()    
test_sum_s_list()        
        
