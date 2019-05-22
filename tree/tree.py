
class SimpleTreeNode:
    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []
                    
class SimpleTree:
    
    def __init__(self, root):
        self.root = root
        self.current = root
        self.__number_node = None
        self.__leaf_number = None
                
    def AddChild(self, ParentNode, NewChild):
        """Добавляет текущему узлу новый узел в качестве дочернего"""
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode
            
    def DeleteNode(self, NodeToDelete):
        """Удаляет существующий некорневой узел NodeToDelete"""
        if NodeToDelete.NodeValue is self.root:
            return
        if NodeToDelete.Children: 
            for child in NodeToDelete.Children:
                child.Parent = NodeToDelete.Parent
                NodeToDelete.Parent.Children.append(child)
            NodeToDelete.Children = []    
        NodeToDelete.Parent.Children.remove(NodeToDelete)  
        NodeToDelete.Parent = None
    
    def GetAllNodes(self):
        """Обходит дерево и составляет список всех узлов в произвольном порядке"""
        def iter(node, lst):
            lst.append(node)
            if node.Children:
                for child in node.Children:
                    iter(child, lst)
            return lst
        return iter(self.root, [])
        
    def FindNodesByValue(self, val):
        """Обходит дерево и составляет список всех узлов с заданным значением"""
        def iter(node, lst):
            if node.NodeValue == val:
                lst.append(node)
            if node.Children:
                for child in node.Children:
                    iter(child, lst)
            return lst
        return iter(self.root, [])
       
    def MoveNode(self, OriginalNode, NewParent):
        """Перемещает некорневой узел вместе с поддеревом дочерним узлом в другое место дерева"""
        if OriginalNode is self.root:
            return
        OldParent = OriginalNode.Parent
        OldParent.Children.remove(OriginalNode)
        self.AddChild(NewParent, OriginalNode)
        
    def Count(self):
        """Возвращает количество всех узлов в дереве"""
        self.__number_node = 0
        def iter(node):
            self.__number_node += 1
            if node.Children:
                for child in node.Children:
                    iter(child)
            return self.__number_node
        return iter(self.root)
        
    def LeafCount(self):
        """Возвращает количество листьев в дереве"""
        self.__leaf_number = 0
        def iter(node):
            if node.Children:
                for child in node.Children:
                    iter(child)
            else:
                self.__leaf_number += 1
            return self.__leaf_number
        return iter(self.root)        
    
    def LevelCount(self, node):
        """Возвращает уровень узла"""
        res = 0
        while not node.Parent is None:
            res += 1
            node = node.Parent
        return res