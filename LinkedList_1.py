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
            #return
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

def test_1():
    s_list = LinkedList()
    s_list.add_in_tail(Node(12))
    s_list.add_in_tail(Node(55))
    s_list.add_in_tail(Node(128))
    s_list.add_in_tail(Node(55))    
    s_list.remove(12)
    
def test_2():
    s_list = LinkedList()
    s_list.add_in_tail(Node(12))
    s_list.add_in_tail(Node(55))
    s_list.add_in_tail(Node(128))
    s_list.add_in_tail(Node(55))    
    s_list.remove(55)
def test_3():
    s_list = LinkedList()
    s_list.add_in_tail(Node(128))
    s_list.add_in_tail(Node(55))
    s_list.remove(128)
    if s_list.head.value != 55:
        print("TEST 3 ERROR", list.head.value)
test_1()
test_2()
test_2()

"""
s_list = LinkedList()
s_list.add_in_tail(Node(12))
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(128))
s_list.add_in_tail(Node(55))

s_list_2 = LinkedList()
s_list_2.add_in_tail(Node(120))
s_list_2.add_in_tail(Node(550))
s_list_2.add_in_tail(Node(1280))
s_list_2.add_in_tail(Node(550))
"""
#print(sum_s_list(s_list, s_list_2))
#s_list.print_all_nodes()
#s_list.remove_one()
#s_list.print_all_nodes()
#s_list.remove(12)
#s_list.remove_all_value(12)
#s_list.print_all_nodes()
#print(s_list.get_length())
#s_list.print_all_nodes()
#s_list.find_all_nodes(55)
#print(s_list.find_all_nodes(55))
