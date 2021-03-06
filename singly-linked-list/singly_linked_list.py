
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
        prevNode = None
        while node is not None:
            if node.value == val:
                # Если единственный элемент
                if node is self.head and node is self.tail:
                    self.head = None
                    self.tail = None
                    
                # Если val в голове списка:
                elif node is self.head:
                    self.head = node.next
                                   
                # Если val в конце списка:
                elif node is self.tail:
                    # Если всего два элемента в списке:
                    if self.head is prevNode:
                        self.head.next = None
                        self.tail = None
                    # Если больше, чем два элемента:    
                    else:
                        prevNode.next = None
                        self.tail = prevNode
                # Если val в середине списка: 
                else:
                    prevNode.next = node.next
                if all == False:
                    return
            else:
                prevNode = node
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
                new_node = newNode
                temp = node.next
                node.next = new_node
                new_node.next = temp
                return
            return iter(node.next)    
        return iter(self.head)
