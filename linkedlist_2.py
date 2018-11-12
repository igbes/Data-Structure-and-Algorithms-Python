class Node2:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
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
            
    def insert(self, item, itemIns):
        # Метод вставки узла после заданного узла
        def iter(node):
            if node is None:
                print("value missing")
                return
            if node.value == item:
                newNode = Node2(itemIns)
                temp = node.next
                node.next = newNode
                newNode.prev = node
                newNode.next = temp
                temp.prev = newNode
                return
            return iter(node.next)    
        return iter(self.head)
    
    def insert_in_head(self, item):
        # Вставка узла первым элементом
        newNode = Node2(item)
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        
    
def get_list_nodes(item):
    # Получить список узлов (вспомогательная функция)
    def iter(node, acc):
        if node is None:
            return acc
        acc.append(node.value)
        return iter(node.next, acc)    
    return iter(item.head, [])    

def test_remove():
    s_list = LinkedList2()
    s_list.add_in_tail(Node2(73))
    s_list.add_in_tail(Node2(73))
    s_list.add_in_tail(Node2(12))            
    s_list.add_in_tail(Node2(12))       
    s_list.add_in_tail(Node2(73))
    s_list.remove(12)
    if get_list_nodes(s_list) == [73, 73, 12, 73]:
        print("test remove(item) is OK")
    else:
        print("test remove(item) is FAIL")
def test_insert():
    s_list_2 = LinkedList2()
    s_list_2.add_in_tail(Node2(12))
    s_list_2.add_in_tail(Node2(38))
    s_list_2.add_in_tail(Node2(12))
    s_list_2.add_in_tail(Node2(55))
    s_list_2.insert(38, 73)
    if get_list_nodes(s_list_2) == [12, 38, 73, 12, 55]:
        print("test insert(item_1, item_2) is OK")
    else:
        print("test insert(item_1, item_2) is FAIL")        

def test_insert_in_head():
    s_list_3 = LinkedList2()
    s_list_3.add_in_tail(Node2(12))
    s_list_3.add_in_tail(Node2(38))
    s_list_3.add_in_tail(Node2(73))
    s_list_3.insert_in_head(100)
    if get_list_nodes(s_list_3) == [100, 12, 38, 73]:
        print("test test_insert_in_head()(item) is OK")
    else:
        print("test test_insert_in_head()(item) is FAIL")
    

        
test_remove() 
test_insert()
test_insert_in_head()