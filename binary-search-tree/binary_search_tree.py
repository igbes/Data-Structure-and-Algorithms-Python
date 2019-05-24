
class BSTNode:
	
    def __init__(self, key, val, parent):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок


class BSTFind: # промежуточный результат поиска

    def __init__(self):
        self.Node = None # None если не найден узел,
        # и в дереве только один корень

        self.NodeHasKey = False # True если узел найден
        self.ToLeft = False # True, если родительскому узлу надо 
        # добавить новый узел левым потомком

class BST:

    def __init__(self, node):
        self.Root = node # корень дерева, или None

    def FindNodeByKey(self, key):
        """ищет в дереве узел и сопутствующую информацию по ключу"""
        node = self.Root
        while node.NodeKey != key:
            if key < node.NodeKey:
                if node.LeftChild is not None:
                    node = node.LeftChild
                else:
                    res = BSTFind()
                    res.Node = node
                    res.ToLeft = True
                    return res
            else:
                if node.RightChild is not None:
                    node = node.RightChild
                else:
                    res = BSTFind()
                    res.Node = node
                    return res
        res = BSTFind()
        res.Node = node
        res.NodeHasKey = True
        return res   
        
    def AddKeyValue(self, key, val):
        """добавляет ключ-значение в дерево"""
        res_find = self.FindNodeByKey(key)
        if res_find.NodeHasKey:
            return False # если ключ уже есть
        node = BSTNode(key, val, res_find.Node)
        if res_find.ToLeft:
            res_find.Node.LeftChild = node
        else:
            res_find.Node.RightChild = node
        return True    
            
    def FinMinMax(self, FromNode, FindMax):
        """ищет максимальный ключ в поддереве, начиная с заданного узла"""
        node = FromNode
        if FindMax == True:
            while node.RightChild is not None:
                node = node.RightChild
        elif FindMax == False:
            while node.LeftChild is not None:
                node = node.LeftChild
        else:
            return None
        return node
    
    def DeleteNodeByKey(self, key):
        """удаляет узел по ключу"""
        res_find = self.FindNodeByKey(key)
        if not res_find.NodeHasKey:
            return False
        del_node = res_find.Node
        if del_node.LeftChild is None and del_node.RightChild is None:
            if del_node.Parent.LeftChild == del_node:
                del_node.Parent.LeftChild = None
            else:
                del_node.Parent.RightChild = None
            del_node.Parent = None
            return True               
        def iter(node):
            if node.LeftChild is None and node.RightChild is None:
                if node.Parent.LeftChild == node:
                    node.Parent.LeftChild = None
                else:
                    node.Parent.RightChild == None
                node.Parent = del_node.Parent
                if del_node.Parent.LeftChild == del_node:
                    del_node.Parent.LeftChild = node
                else:
                    del_node.Parent.RightChild = node
                if del_node.LeftChild != node:
                    node.LeftChild = del_node.LeftChild
                else:
                    node.LeftChild = None
                if del_node.RightChild != node:
                    node.RightChild = del_node.RightChild
                else:
                    node.RightChild = None
                del_node.Parent = None
                del_node.LeftChild = None
                del_node.RightChild = None
                return True
            if node.LeftChild:    
                return iter(node.LeftChild)
            else:
                return iter(node.RightChild)
        return iter(del_node.RightChild)          
           
    def Count(self):
        """возвращает количество узлов в дереве"""
        return len(self.GetNodeList())
    
    def GetNodeList(self):
        """возвращает список узлов в дереве"""
        def iter(node, lst):
            lst.append(node)
            if node.LeftChild is not None:
                iter(node.LeftChild, lst)
            if node.RightChild is not None:
                iter(node.RightChild, lst)
            return lst
        return iter(self.Root, [])        
        