class Node:
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
    
    # 2.1
    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None
    
    # 2.2
    def find_all(self, val):
        """Возвращает список узлов по заданному значению"""
        def iter(node, acc):
            if node is None:
                return acc
            if node.value == val:
                acc.append(node)
            return iter(node.next, acc)    
        return iter(self.head, [])
    
    # 2.3 - 2.4  
    def delete(self, val, all=False):
        """Удаляет один или все узлы по значению,
         по умолчанию удаляется первый нашедшийся элемент"""
        node = self.head
        while node is not None:
            if node.value is val:
                
                # Если единственный элемент:
                if node is self.head and node is self.tail:
                    self.head = None
                    self.tail = None
                    
                # Если val в голове списка:
                elif node is self.head:
                    self.head = node.next
                    self.head.prev = None
                
                # Если val в конце списка:
                elif node is self.tail:
                    self.tail = node.prev
                    self.tail.next = None
                    node.prev = None
                    
                # Если val в середине списка:
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    
                if all == False:
                    return
            node = node.next
    
    # 2.5        
    def insert(self, afterNode, newNode):
        """Вставляет узел после заданного узла"""
        if afterNode is newNode:
            return 
        if self.head == None and afterNode == None:
            self.add_in_tail(newNode)
            return        
        def iter(node):
            if node is None:
                return
            if node is newNode:
                return            
            if node is afterNode:
                if node is self.tail:
                    self.add_in_tail(newNode)
                    return                
                temp = node.next
                node.next = newNode
                newNode.prev = node
                newNode.next = temp
                temp.prev = newNode
                return
            return iter(node.next)    
        return iter(self.head)
    
    # 2.6
    def add_in_head(self, newNode):
        # Вставка узла первым элементом
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        newNode.prev = None
    # 2.7
    def clean(self):
        """Очищает содержимое списка (создание пустого списка)"""
        self.head = None
        self.tail = None        
        
    # 2.8
    def len(self):
        """Возвращает длину списка"""
        def iter(node, acc):
            if node is None:
                return acc
            return iter(node.next, acc + 1)
        return iter(self.head, 0)
        
    
