import unittest
import random
import time

class TreeNode:
    def __init__(self, key, parent):
        
        self.parent = parent 
        self.key = key
        self.left = None
        self.right = None
        self.color = None
        
        """Поля ниже задействуются при связывании листьев двух деревьев"""
        self.left_color = None
        self.right_color = None

class BinaryWeldedTree:
    
    def __init__(self, depth):
        
        self.depth = depth
        self.root_up = TreeNode(1, None)
        self.root_down = TreeNode(self.get_mumber_nodes(self.depth) * 2, None)        
        self.current = None
        self.color = ['blue', 'green', 'red', 'ellow']
        
        self.visual_form_up = None    # строка визуального представления верхнего дерева
        self.visual_form_down = None  # строка визуального представления нижнего дерева
        
        self.leaves_up = None
        self.leaves_down = None
        
        # Визуальное представление листьев и их связей верхнего и, соответственно, нижнего дерева:
        self.visual_leaves_up = None    
        self.visual_leaves_down = None
        
        # флаг успешности завершения расстановки цветов в связях между листьями деревьев,
        # в случае успешности flag = 1
        self.flag = 0 
        
        # Содержит узел, установленный функцией get_node()
        self.current = None
        
    def getBWT(self, symmetry = True):
        
        self.visual_form_up = '1\n'
        size_tree = self.get_mumber_nodes(self.depth) * 2
        self.visual_form_down = '{0}\n'.format(size_tree)
        
        def iter(array_children_up, array_children_down, key_up, key_down, depth):
            
            if depth == self.depth:
                self.leaves_up = array_children_up
                self.leaves_down = array_children_down
                return
            
            arr_up = []
            arr_down = []
            for child in array_children_up:
                new_color = self.color[:]
                key_up += 1
                child.left = TreeNode(key_up, child)
                child.left.color = self.choice_element(new_color, child.color)
                key_up += 1
                child.right = TreeNode(key_up, child)
                child.right.color = self.choice_element(new_color, child.left.color)
                arr_up.append(child.left)
                arr_up.append(child.right)
                new_arr_up = arr_up[:]
            
                self.visual_form_up += child.left.color
                self.visual_form_up += ' '
                self.visual_form_up += str(child.left.key)
                self.visual_form_up += ' '
                self.visual_form_up += child.right.color
                self.visual_form_up += ' '
                self.visual_form_up += str(child.right.key)
                self.visual_form_up += ' '
                
            i = 0    
            for child in array_children_down:
                new_color_down = self.color[:]
                key_down -= 1
                child.left = TreeNode(key_down, child)
                if symmetry:
                    child.left.color = arr_up[i].color
                    i += 1
                else:    
                    child.left.color = self.choice_element(new_color_down, child.color)
                key_down -= 1
                child.right = TreeNode(key_down, child)
                if symmetry:
                    child.right.color = arr_up[i].color
                    i += 1
                else:    
                    child. right.color = self.choice_element(new_color_down, child.left.color)
                arr_down.append(child.left)
                arr_down.append(child.right)
                new_arr_down = arr_down[:]
                                                    
                self.visual_form_down += child.left.color
                self.visual_form_down += ' '
                self.visual_form_down += str(child.left.key)
                self.visual_form_down += ' '
                self.visual_form_down += child.right.color
                self.visual_form_down += ' '
                self.visual_form_down += str(child.right.key)
                self.visual_form_down += ' '                   
               
            self.visual_form_up += '\n'
            self.visual_form_down += '\n'
            
            return iter(new_arr_up, new_arr_down, key_up, key_down, depth + 1)
        iter([self.root_up], [self.root_down], self.root_up.key, self.root_down.key, 0)
        
    def bind_trees(self):
        
        def get_color_leaf(element_up, element_down):
            
            """Возвращает цвет связи между лисьтьями спаянных деревьев"""
            leaf_color = self.color[:]
            if element_up.left == None:
                element_up_other_color = element_up.right_color
            else:
                element_up_other_color = element_up.left_color
            if element_down.left == None:
                element_down_other_color = element_down.right_color
            else:
                element_down_other_color = element_down.left_color
            res = self.choice_element(leaf_color, element_up.color, element_down.color, element_up_other_color, element_down_other_color) 
            return res 
        
        array_children_up = self.leaves_up
        array_children_down = self.leaves_down[:]
        
        def is_element_down_right(element):
            
            """Возвращает True если узел содержит только element.right""" 
            if element.left == None:
                return False
            return True
        
        for element_up in self.leaves_up:
            element_down_left = random.choice(array_children_down)
            element_up.left = element_down_left
            if is_element_down_right(element_down_left):
                f = "right"
                element_down_left.right = element_up
            else:
                f = "left"
                element_down_left.left = element_up
            try: 
                color = get_color_leaf(element_up, element_down_left)
            except IndexError:
                self.flag = 0
                tree = None
                self.leaves_up = None
                self.leaves_down = None
                print("failed to bind the leaves! try again!!!")
                return
            element_up.left_color = color
            if f == "right":
                element_down_left.right_color = color
            else:
                element_down_left.left_color = color
            arr_down = array_children_down[:]
            element_down_right = self.choice_element(arr_down, element_down_left)
            if element_up.key != self.get_mumber_nodes(self.depth) and element_down_left.left and element_down_right.left:
                arr_down.remove(element_down_right)
                element_down_right = random.choice(arr_down)
            element_up.right = element_down_right
            if is_element_down_right(element_down_right):
                f = "right"
                element_down_right.right = element_up
            else:
                f = "left"
                element_down_right.left = element_up
            try: 
                color = get_color_leaf(element_up, element_down_right)
            except IndexError:
                self.flag = 0
                tree = None
                self.leaves_up = None
                self.leaves_down = None
                print("failed to bind the leaves! try again!!!")   
                return
            element_up.right_color = color
            if f == "right":
                element_down_right.right_color = color
            else:
                element_down_right.left_color = color
            arr_down = array_children_down[:]
            if element_down_left.right:
                array_children_down.remove(element_down_left)
            if element_down_right.right:
                array_children_down.remove(element_down_right)
            
        self.leaves_up = array_children_up
        self.flag = 1
       
    def get_visual_leaves_up(self):
        
        if self.flag == 0:
            return 
        self.visual_leaves_up = {}
        for element in self.leaves_up:
            self.visual_leaves_up[element.key] = {}
            self.visual_leaves_up[element.key].update({"left": element.left.key})
            self.visual_leaves_up[element.key].update({"left_color": element.left_color})
            self.visual_leaves_up[element.key].update({"right": element.right.key})
            self.visual_leaves_up[element.key].update({"right_color": element.right_color})
            
    def get_visual_leaves_down(self):
        
        if self.flag == 0:
            return
        self.visual_leaves_down = {}
        for element in self.leaves_down:
            self.visual_leaves_down[element.key] = {}
            self.visual_leaves_down[element.key].update({"left": element.left.key})
            self.visual_leaves_down[element.key].update({"left_color": element.left_color})
            self.visual_leaves_down[element.key].update({"right": element.right.key})
            self.visual_leaves_down[element.key].update({"right_color": element.right_color})  
    
    def get_mumber_nodes(self, depth_number):
        """ Определяет количество узлов верхнего дерева, принимает в
        качестве аргумента глубину дерева"""
        depth_counter = 0
        res = 1
        node_children = 2
        children_number = 1
        while depth_counter < depth_number:
            depth_counter += 1
            children_number *= node_children 
            res += children_number
        return res

    def choice_element(self, arr, *exeption_elements):
        """Возвращает случайный элемент из заданного списка, исключая exeption_elements"""
        for element in exeption_elements:
            if element in arr:
                arr.remove(element)
        return random.choice(arr) 
    
    def get_node(self, key_node):
        """Возвращает узел дерева по ключу"""
        if self.flag == 0 or key_node > self.root_down.key:
            return
        if key_node <= self.root_down.key / 2:
            root = self.root_up
        else:
            root = self.root_down
        def iter(node):
            
            if node.key == key_node:
                self.current = node
                res = node
            if node.left_color != None and node.right_color != None:
                return #res
            children = [node.left, node.right]
            for child in children:
                iter(child)
        iter(root)
        
        return self.current
       
    def get_path(self, color, value_color = 'min'):
        
        if self.flag == 0:
            return        
        def tree_traversal(root):
            
            res_dict = {}
            def iter(node, count):
                if node.left_color != None and node.right_color != None:
                    res_dict.update({node.key: count})
                    return
            
                if node.left.color == color:
                    iter(node.left, count + 1)
                else:
                    iter(node.left, count)
                if node.right.color == color:
                    iter(node.right, count + 1)
                else:
                    iter(node.right, count)
                    
            iter(root, 0)
            return res_dict
        
        dict_up = tree_traversal(self.root_up)
        dict_down = tree_traversal(self.root_down)
        
        connection_leaves = {}
        
        for key_up, value in self.visual_leaves_up.items():
            key_down_left = value['left']
            if value['left_color'] == color:
                color_value = 1
            else:
                color_value = 0
            key_connect = '{0} - {1}'.format(key_up, key_down_left)
            connection_leaves.update({key_connect: dict_up[key_up] + dict_down[key_down_left] + color_value})
            
            key_down_right = value['right']
            if value['right_color'] == color:
                color_value = 1
            else:
                color_value = 0
            key_connect = '{0} - {1}'.format(key_up, key_down_right)
            connection_leaves.update({key_connect: dict_up[key_up] + dict_down[key_down_right] + color_value}) 
        
        res = {}    
        sorted_value = sorted(val for val in connection_leaves.values())
        if value_color == 'max':
            sorted_value.reverse()
        for item in sorted_value:    
            for key, value in connection_leaves.items():
                if value == item:
                    res.update({key: value})
        return res
    
    def get_wandering_search_1(self, key_node):
        """Алгоритм случайного блуждания.
        Возвращает количество шагов."""
        
        if self.flag == 0:
            return
        node = self.root_up
        count = 0
        while node is not key_node:
            if node == self.root_up:
                node = random.choice([node.left, node.right])
            else:    
                node = random.choice([node.parent, node.left, node.right])
            count += 1
        self.current = node    
        return count    
    
    def get_wandering_search_2(self, any_node):
        """Алгоритм случайного квантового блуждания.
        Возвращает количество шагов."""
        
        if self.flag == 0:
            return
        list_node = [self.root_up]
        count = 0
        for node in list_node:
            count += 1
            if node is any_node:
                self.current = node
                return count
            if node == self.root_up:
                list_node.append(random.choice([node.left, node.right]))
            else:    
                list_node.append(random.choice([node.parent, node.left, node.right]))
            
    
tree = BinaryWeldedTree(3)
tree.getBWT(False)
#tree.getBWT()
print(tree.visual_form_up)
print(tree.visual_form_down)
tree.bind_trees()
tree.get_visual_leaves_up()
print("visual_up :", tree.visual_leaves_up)
tree.get_visual_leaves_down()
print("visual_down :", tree.visual_leaves_down)
#print(tree.tree_traversal(tree.root_up, 'red'))
#print(tree.tree_traversal(tree.root_down, 'red'))

print('\n max', tree.get_path('red', 'max'))

print('\n min', tree.get_path('red'))

#print('\n key', tree.get_node(25).key)
#node_f = tree.get_node(25)
#print('\n node_f.key', node_f.key)
#print('\n node_f.parent.key', node_f.parent.key)



a = time.time()  
#print('\n get_wandering_search_1()', tree.get_wandering_search_1(tree.root_down))
#b = time.time()
#print('секунд :',b - a)
#print('\n current.key', tree.current.key)

a = time.time()  
print('\n get_wandering_search_2()', tree.get_wandering_search_2(tree.root_down))
b = time.time()
print('секунд :',b - a)
print('\n current.key', tree.current.key)
