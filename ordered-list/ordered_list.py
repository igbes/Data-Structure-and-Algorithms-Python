
class Node:
    
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc
    
    def compare(self, v1, v2):
        """Сравненивает элементы по значению"""
        if v1 == v2:
            return 0        
        if self.__ascending == True:
            if v1 < v2:
                return -1
            if v1 > v2:
                return 1
        if self.__ascending == False:
            if v1 > v2:
                return -1
            if v1 < v2:
                return 1
        
    def add(self, value):
        """Добавляет узел по значению в упорядоченный список"""
        def insert(afterNode, newNode):
            """Вставляет узел после заданного узла"""
            def iter(node):
                if node is None:
                    return
                if node is afterNode:
                    if node is self.tail:
                        add_in_tail(newNode)
                        return                
                    temp = node.next
                    node.next = newNode
                    newNode.prev = node
                    newNode.next = temp
                    temp.prev = newNode
                    return
                return iter(node.next)    
            return iter(self.head)
        
        def add_in_head(newNode):
            """Вставляет узел первым элементом"""
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            newNode.prev = None
        
        def add_in_tail(item):
            """Вставляет узел в хвост списка"""
            if self.head is None:
                self.head = item
                item.prev = None
                item.next = None
            else:
                self.tail.next = item
                item.prev = self.tail
            self.tail = item
        
        new_node = Node(value)
        # Если список пустой:
        if self.head is None:
            # Если список пуст - создать список с единственным элементом
            add_in_tail(new_node)
            return
            
        if self.compare(new_node.value, self. head.value) == -1:
            # вставить в голову
            add_in_head(new_node)
            return
                  
        # Если элемент больше значения хвоста:
        if self.compare(new_node.value, self.tail.value) == 1:
            # вставить в хвост
            add_in_tail(new_node)
            return
            
        node = self.head
        while True:
            if self.compare(node.value, new_node.value) == -1 and self.compare(new_node.value, node.next.value) == -1 or self.compare(node.value, new_node.value) == 0:
                # вставить после node
                insert(node, new_node)
                return
            node = node.next
       
    def find(self, val):
        """Возвращает элемент по значению"""
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            if self.compare(val, node.value) == -1:
                return None
            node = node.next
        return None    
    
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
                return
            node = node.next
    
    def clean(self, asc):
        """Очищает содержимое списка (создание пустого списка)"""
        self.__ascending = asc
        self.head = None
        self.tail = None  
    
    def len(self):
        """Возвращает длину списка"""
        def iter(node, acc):
            if node is None:
                return acc
            return iter(node.next, acc + 1)
        return iter(self.head, 0)
    
    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r
        
class OrderedStringList(OrderedList):
    
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc
                
    def compare(self, v1, v2):
        """Сравненивает элементы по значению"""
        new_v1 = v1.strip().rstrip()
        new_v2 = v2.strip().rstrip()
        if v1 == v2:
            return 0        
        if self.__ascending == True:
            if new_v1 < new_v2:
                return -1
            if new_v1 > new_v2:
                return 1
        if self.__ascending == False:
            if new_v1 > new_v2:
                return -1
            if new_v1 < new_v2:
                return 1        
