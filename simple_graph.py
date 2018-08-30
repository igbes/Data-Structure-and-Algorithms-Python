import unittest

class SimpleGraph:
    
    def __init__(self, max_vertex):
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
        if add == 1:        
            self.m_adjacency[index_1][index_2], self.m_adjacency[index_2][index_1] = 1, 1
        else:
            self.m_adjacency[index_1][index_2], self.m_adjacency[index_2][index_1] = 0, 0
        
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
        
    def test_del_vertex_with_edge(self):
        """
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
                         
if __name__ == '__main__':
    unittest.main()      
 