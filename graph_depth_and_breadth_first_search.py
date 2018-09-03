import unittest

class SimpleGraph:
    
    def __init__(self, max_vertex, oriented = 0):
        self.oriented = oriented
        self._max_vertex = max_vertex
        self.m_adjacency = [[0] * max_vertex for i in range(max_vertex)]
        self.list_vertex = [] 
        
    def add_vertex(self, value):
        """
        Добавляет вершину (тип данных - строка)
        """
        if isinstance(value, str) and len(self.list_vertex) < self._max_vertex:
            if not (value in self.list_vertex):
                self.list_vertex.append(value)
                #self.hit[value] = None 
                return value
        else:
            return -1
        
    def add_del_edge(self, vert_1, vert_2, add = 1):
        """
        Добавляет ребра между узлами, если add = 1, иначе - удаляет
        """
        index_1, index_2 = None, None
        for index, value in enumerate(self.list_vertex):
            if value == vert_1:
                index_1 = index
            if value == vert_2:
                index_2 = index
        if index_1 == None or index_2 == None: 
            return -1
        if self.oriented == 0:
            if add == 1:        
                self.m_adjacency[index_1][index_2], self.m_adjacency[index_2][index_1] = 1, 1
            else:
                self.m_adjacency[index_1][index_2], self.m_adjacency[index_2][index_1] = 0, 0
        else:
            if add == 1:        
                self.m_adjacency[index_1][index_2] = 1            
            else:
                self.m_adjacency[index_1][index_2] = 0            
             
    def del_vertex_with_edge(self, vert):
        """
        Удаляет вершину (присваивает значение None в списке) и все её рёбра
        """
        index_vert = None
        for index, value in enumerate(self.list_vertex):
            if value == vert:
                index_vert = index
                self.list_vertex[index_vert] = None
                break
        if index_vert == None:
            return -1
        for i in range(index_vert + 1):
            self.m_adjacency[i][index_vert], self.m_adjacency[index_vert][i] = 0, 0
            
    def search_depth(self, item, to_item):
        """
        Поиск в глубину.
        Возвращает:
        True, если путь до вершины существует,
        False, если путь до вершины отсутствует, или первый и второй параметр совпадают
        -1, если отстутствует хоть одна из заданных в параметрах вершин
        """
        self.stack = []
        self.stack_index = []
        self.hit = dict.fromkeys(self.list_vertex)
        vert, to_vert = None, None
        for i, vertex in enumerate(self.list_vertex):
            if vertex == item:
                vert = item
                index = i
            if vertex == to_item:
                to_vert = to_item
        if not (vert and to_vert):
            return -1
        self.stack.append(vert)   
        self.stack_index.append(index)
        self.hit[vert] = True
        while self.stack:
            for ind, value in enumerate(self.m_adjacency[index]): 
                if value and not self.hit[self.list_vertex[ind]]:
                    vert = self.list_vertex[ind]
                    if vert == to_vert:
                        return True
                    self.stack.append(vert)
                    self.hit[vert] = True
                    index = ind
                    self.stack_index.append(index)
                    break
                if ind == len(self.list_vertex) - 1:
                    self.stack.pop()
                    self.stack_index.pop()
                    if len(self.stack): 
                        vert = self.stack[-1]
                        index = self.stack_index[-1]
        return False          
    
    def search_breadth(self, item, to_item):
        """ 
        Поиск в ширину.
        Возвращает:
        Список, содержащий путь, если путь до вершины существует,
        False, если путь до вершины отсутствует, или первый и второй параметр совпадают
        -1, если отстутствует хоть одна из заданных в параметрах вершин    
        """
        self.queue = []
        self.hit = dict.fromkeys(self.list_vertex)
        self.dict_index = {key: value for value, key in enumerate(self.list_vertex)}
        self.path = []
        vert, to_vert = None, None
        for i, vertex in enumerate(self.list_vertex):
            if vertex == item:
                vert = item
                index = i
            if vertex == to_item:
                to_vert = to_item
        if not (vert and to_vert):
            return -1        
        self.queue.append(vert)
        self.hit[vert] = True
        #self.path.append(vert)
        while self.queue:
            vert = self.queue.pop(0)
            index = self.dict_index[vert]
            if 1 in self.m_adjacency[index]:###
                self.path.append(vert)      ###
            for ind, value in enumerate(self.m_adjacency[index]):
                if value and not self.hit[self.list_vertex[ind]]:
                    vert = self.list_vertex[ind]
                    if vert == to_vert:
                        #return True
                        self.path.append(vert)
                        return self.path
                    self.queue.append(vert)
                    self.hit[vert] = True                       
        return False


class TestSimpleGraph(unittest.TestCase):
    
    def setUp(self):
        self.my_graph = SimpleGraph(5)  
        self.my_graph.add_vertex('A')
        self.my_graph.add_vertex('B')
        self.my_graph.add_vertex('C')
        self.my_graph.add_vertex('D')
        self.my_graph.add_vertex('E')
        self.my_graph.add_vertex('A')        
    
    def test_add_vertex(self):
        """
        Проверка создания пустой матрицы смежности и добавления вершин 
        """
        self.assertEqual(self.my_graph.m_adjacency, 
                         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
        self.assertEqual(self.my_graph.list_vertex, ['A', 'B', 'C', 'D', 'E'])
        self.assertAlmostEqual(self.my_graph.add_vertex(28), -1)
        self.assertEqual(self.my_graph.list_vertex, ['A', 'B', 'C', 'D', 'E'])
        
    def test_add_del_edge(self):
        
        """
        НЕОРИЕНТИРОВАННЫЙ ГРАФ:
        
        Проверка добавления рёбер
        """
        self.my_graph.add_del_edge('A', 'B')
        self.my_graph.add_del_edge('A', 'C')
        self.my_graph.add_del_edge('A', 'D')
        self.my_graph.add_del_edge('B', 'D')
        self.my_graph.add_del_edge('B', 'E')
        self.my_graph.add_del_edge('C', 'D')
        self.my_graph.add_del_edge('D', 'D')
        self.my_graph.add_del_edge('D', 'E') 
        
        self.assertEqual(self.my_graph.m_adjacency, 
                         [[0, 1, 1, 1, 0], [1, 0, 0, 1, 1], [1, 0, 0, 1, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0]])
        """
        Проверка добавления/удаления ребра к несуществующему узлу
        """
        self.assertEqual(self.my_graph.add_del_edge('A', 's'), -1)
        self.assertEqual(self.my_graph.add_del_edge('A', 's', 0), -1)
        
        """
        Проверка удаления ребра
        """
        self.my_graph.add_del_edge('A', 'D', 0)
        self.assertEqual(self.my_graph.m_adjacency, 
                         [[0, 1, 1, 0, 0], [1, 0, 0, 1, 1], [1, 0, 0, 1, 0], [0, 1, 1, 1, 1], [0, 1, 0, 1, 0]]) 
        """
        ОРИЕНТИРОВАННЫЙ ГРАФ:
        
        Проверка добавления рёбер
        """
        self.my_graph = SimpleGraph(5, 1)  
        self.my_graph.add_vertex('A')
        self.my_graph.add_vertex('B')
        self.my_graph.add_vertex('C')
        self.my_graph.add_vertex('D')
        self.my_graph.add_vertex('E')
        self.my_graph.add_vertex('A')
        
        self.my_graph.add_del_edge('A', 'B')
        self.my_graph.add_del_edge('A', 'C')
        self.my_graph.add_del_edge('A', 'D')
        self.my_graph.add_del_edge('B', 'D')
        self.my_graph.add_del_edge('B', 'E')
        self.my_graph.add_del_edge('C', 'D')
        self.my_graph.add_del_edge('D', 'D')
        self.my_graph.add_del_edge('D', 'E') 
        
        self.assertEqual(self.my_graph.m_adjacency, 
                         [[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 0, 0, 1, 1], [0, 0, 0, 0, 0]])
        """
        Проверка добавления/удаления ребра к несуществующему узлу
        """
        self.assertEqual(self.my_graph.add_del_edge('A', 's'), -1)
        self.assertEqual(self.my_graph.add_del_edge('A', 's', 0), -1)
        
        """
        Проверка удаления ребра
        """
        self.my_graph.add_del_edge('A', 'D', 0)
        self.assertEqual(self.my_graph.m_adjacency, 
                         [[0, 1, 1, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 0, 0, 1, 1], [0, 0, 0, 0, 0]]) 
        
    def test_del_vertex_with_edge(self):
        """
        НЕОРИЕНТИРОВАННЫЙ ГРАФ:
        
        Проверка удаления узла со всеми рёбрами
        """
        self.my_graph.add_del_edge('A', 'B')
        self.my_graph.add_del_edge('A', 'C')
        self.my_graph.add_del_edge('A', 'D')
        self.my_graph.add_del_edge('B', 'D')
        self.my_graph.add_del_edge('B', 'E')
        self.my_graph.add_del_edge('C', 'D')
        self.my_graph.add_del_edge('D', 'D')
        self.my_graph.add_del_edge('D', 'E')
        
        self.my_graph.del_vertex_with_edge('E')
        self.assertEqual(self.my_graph.list_vertex, ['A', 'B', 'C', 'D', None])
        self.assertEqual(self.my_graph.m_adjacency, 
                         [[0, 1, 1, 1, 0], [1, 0, 0, 1, 0], [1, 0, 0, 1, 0], [1, 1, 1, 1, 0], [0, 0, 0, 0, 0]])
        """
        ОРИЕНТИРОВАННЫЙ ГРАФ:
        
        Проверка удаления узла со всеми рёбрами
        """
        self.my_graph = SimpleGraph(5, 1)  
        self.my_graph.add_vertex('A')
        self.my_graph.add_vertex('B')
        self.my_graph.add_vertex('C')
        self.my_graph.add_vertex('D')
        self.my_graph.add_vertex('E')
        self.my_graph.add_vertex('A')         
            
        self.my_graph.add_del_edge('A', 'B')
        self.my_graph.add_del_edge('A', 'C')
        self.my_graph.add_del_edge('A', 'D')
        self.my_graph.add_del_edge('B', 'D')
        self.my_graph.add_del_edge('B', 'E')
        self.my_graph.add_del_edge('C', 'D')
        self.my_graph.add_del_edge('D', 'D')
        self.my_graph.add_del_edge('D', 'E')
        
        self.my_graph.del_vertex_with_edge('E')
        self.assertEqual(self.my_graph.list_vertex, ['A', 'B', 'C', 'D', None])
        self.assertEqual(self.my_graph.m_adjacency, 
                         [[0, 1, 1, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0]])
    
    def test_search_depth(self):
        """
        Проверка поиска в глубину
        
        НЕОРИЕНТИРОВАННЫЙ ГРАФ:
        """
        self.my_graph.add_del_edge('A', 'B')
        self.my_graph.add_del_edge('A', 'C')
        self.my_graph.add_del_edge('A', 'D')
        self.my_graph.add_del_edge('B', 'D')
        self.my_graph.add_del_edge('B', 'E')
        self.my_graph.add_del_edge('C', 'D')
        self.my_graph.add_del_edge('D', 'D')
        self.my_graph.add_del_edge('D', 'E')
        
        self.assertEqual(self.my_graph.search_depth("A", "E"), True)
        self.assertEqual(self.my_graph.search_depth("E", "A"), True)
        self.assertEqual(self.my_graph.search_depth("E", "C"), True)
        self.assertEqual(self.my_graph.search_depth("C", "B"), True)
        self.assertEqual(self.my_graph.search_depth("s", "K"), -1)
        self.assertEqual(self.my_graph.search_depth("A", "A"), False)
        
        """
        ОРИЕНТИРОВАННЫЙ ГРАФ:
        """
        self.my_graph = SimpleGraph(5, 1)  
        self.my_graph.add_vertex('A')
        self.my_graph.add_vertex('B')
        self.my_graph.add_vertex('C')
        self.my_graph.add_vertex('D')
        self.my_graph.add_vertex('E')
        self.my_graph.add_vertex('A')
        
        self.my_graph.add_del_edge('A', 'B')
        self.my_graph.add_del_edge('A', 'C')
        self.my_graph.add_del_edge('A', 'D')
        self.my_graph.add_del_edge('B', 'D')
        self.my_graph.add_del_edge('B', 'E')
        self.my_graph.add_del_edge('C', 'D')
        self.my_graph.add_del_edge('D', 'D')
        self.my_graph.add_del_edge('D', 'E')
        
        self.assertEqual(self.my_graph.search_depth("A", "E"), True)
        self.assertEqual(self.my_graph.search_depth("E", "A"), False)
        self.assertEqual(self.my_graph.search_depth("E", "C"), False)
        self.assertEqual(self.my_graph.search_depth("C", "B"), False)
        self.assertEqual(self.my_graph.search_depth("A", "D"), True)
        self.assertEqual(self.my_graph.search_depth("D", "D"), False)
        self.assertEqual(self.my_graph.search_depth("s", "K"), -1)
        self.assertEqual(self.my_graph.search_depth("A", "A"), False)
    
    def test_search_breadth(self):
        """
        Проверка поиска в ширину
        
        НЕОРИЕНТИРОВАННЫЙ ГРАФ:
        """
        self.my_graph.add_del_edge('A', 'B')
        self.my_graph.add_del_edge('A', 'C')
        self.my_graph.add_del_edge('A', 'D')
        self.my_graph.add_del_edge('B', 'D')
        self.my_graph.add_del_edge('B', 'E')
        self.my_graph.add_del_edge('C', 'D')
        self.my_graph.add_del_edge('D', 'D')
        self.my_graph.add_del_edge('D', 'E')
        self.assertEqual(self.my_graph.search_breadth("A", "E"), ['A', 'B', 'E'])
        self.assertEqual(self.my_graph.search_breadth("E", "A"), ['E', 'B', 'A'])
        self.assertEqual(self.my_graph.search_breadth("E", "C"), ['E', 'B', 'D', 'C'])
        self.assertEqual(self.my_graph.search_breadth("C", "B"), ['C', 'A','B'])
        self.assertEqual(self.my_graph.search_breadth("s", "K"), -1)
        self.assertEqual(self.my_graph.search_breadth("A", "A"), False) 
        
        """
        ОРИЕНТИРОВАННЫЙ ГРАФ:
        """
       
        self.my_graph = SimpleGraph(5, 1)  
        self.my_graph.add_vertex('A')
        self.my_graph.add_vertex('B')
        self.my_graph.add_vertex('C')
        self.my_graph.add_vertex('D')
        self.my_graph.add_vertex('E')
        self.my_graph.add_vertex('A')
        
        self.my_graph.add_del_edge('A', 'B')
        self.my_graph.add_del_edge('A', 'C')
        self.my_graph.add_del_edge('A', 'D')
        self.my_graph.add_del_edge('B', 'D')
        self.my_graph.add_del_edge('B', 'E')
        self.my_graph.add_del_edge('C', 'D')
        self.my_graph.add_del_edge('D', 'D')
        self.my_graph.add_del_edge('D', 'E')
        
        self.assertEqual(self.my_graph.search_breadth("A", "E"), ['A', 'B', 'E'])
        self.assertEqual(self.my_graph.search_breadth("E", "A"), False)
        self.assertEqual(self.my_graph.search_breadth("E", "C"), False)
        self.assertEqual(self.my_graph.search_breadth("C", "B"), False)
        self.assertEqual(self.my_graph.search_breadth("A", "D"), ['A', 'D'])
        self.assertEqual(self.my_graph.search_breadth("D", "D"), False)
        self.assertEqual(self.my_graph.search_breadth("s", "K"), -1)
        self.assertEqual(self.my_graph.search_breadth("A", "A"), False)
        
if __name__ == '__main__':
    unittest.main()                 