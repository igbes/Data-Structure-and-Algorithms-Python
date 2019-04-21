
import unittest
from ordered_list import OrderedList
from ordered_list import OrderedStringList

def get_list_nodes(item):
    """Получить список узлов (вспомогательная функция для тестирования)"""
    def iter(node, acc):
        if node is None:
            return acc
        acc.append(node.value)
        return iter(node.next, acc)    
    return iter(item.head, [])

class TestOrderedList(unittest.TestCase):
    """for numbers:"""    
              
    def test_add(self):
                
        self.o_list = OrderedList(True)
        self.o_list.add(7)
        self.o_list.add(6)
        self.o_list.add(4)
        self.o_list.add(10)       
        self.o_list.add(2)        
        self.o_list.add(4)
        res = get_list_nodes(self.o_list)
        self.assertEqual(res, [2, 4, 4, 6, 7, 10])
        self.assertEqual(self.o_list.get_all()[3].value, 6)
        self.assertEqual(self.o_list.get_all()[-1].value, 10)
        
        self.o_list.add(1)
        self.assertEqual(self.o_list.get_all()[0].value, 1)
        res = get_list_nodes(self.o_list)
        self.assertEqual(res, [1, 2, 4, 4, 6, 7, 10])
      
        
        self.o_list = OrderedList(True)
        self.o_list.add(7)
        res = get_list_nodes(self.o_list)
        self.assertEqual(res, [7])    
        
        self.o_list = OrderedList(True)
        self.o_list.add(8)
        self.o_list.add(7)
        #print(self.o_list.get_all())
        self.o_list.add(8)
        #print(self.o_list.get_all())
        res = get_list_nodes(self.o_list)
        self.assertEqual(res, [7, 8, 8])          
        
        self.o_list = OrderedList(False)
        self.o_list.add(7)
        self.o_list.add(6)
        self.o_list.add(4)
        self.o_list.add(10)       
        self.o_list.add(2)        
        self.o_list.add(4)
        res = get_list_nodes(self.o_list)
        self.assertEqual(res, [10, 7, 6, 4, 4, 2]) 
        self.assertEqual(self.o_list.get_all()[3].value, 4)
        self.assertEqual(self.o_list.get_all()[-1].value, 2)        
        
        
        self.o_list = OrderedList(False)
        self.o_list.add(7)
        res = get_list_nodes(self.o_list)
        self.assertEqual(res, [7])
        self.assertEqual(self.o_list.get_all()[-1].value, 7)
        
        self.o_list = OrderedList(False)
        self.o_list.add(7)
        self.o_list.add(8)
        res = get_list_nodes(self.o_list)
        self.assertEqual(res, [8, 7]) 
        self.assertEqual(self.o_list.get_all()[-1].value, 7)
        
    def test_find(self):
        
        self.o_list = OrderedList(True)
        self.o_list.add(7)
        self.o_list.add(6)
        self.o_list.add(4)        
        self.assertEqual(self.o_list.find(6).value, 6)
        self.assertEqual(self.o_list.find(8), None)
    
    def test_delete(self):
        self.o_list = OrderedList(True)
        self.o_list.add(7)
        self.o_list.add(6)
        self.o_list.add(4)
        self.o_list.add(10)
        self.o_list.delete(6)
        res = get_list_nodes(self.o_list)
        self.assertEqual(res, [4, 7, 10])
        
class TestOrderedStringList(unittest.TestCase):
    """for strings:"""
        
    def test_add(self):
        # Вставка узла в середину списка
        self.o_list_str = OrderedStringList(True)
        self.o_list_str.add("ab")
        self.o_list_str.add("ad")
        self.o_list_str.add("ae")
        self.o_list_str.add(" ac  ")
        res = get_list_nodes(self.o_list_str)
        self.assertEqual(res, ["ab", " ac  ", "ad", "ae"])
    
        self.o_list_str = OrderedStringList(True)
        self.o_list_str.add("ab")
        self.o_list_str.add("ad")
        self.o_list_str.add("ae")        
        self.o_list_str.add("  aa")
        res = get_list_nodes(self.o_list_str)
        self.assertEqual(res, ["  aa", "ab", "ad", "ae"])
        
        self.o_list_str = OrderedStringList(False)
        self.o_list_str.add("ab")
        self.o_list_str.add("ad")
        self.o_list_str.add("ae")
        self.o_list_str.add(" ac  ")
        res = get_list_nodes(self.o_list_str)
        self.assertEqual(res, ["ae", "ad", " ac  ", "ab"])    
        
        self.o_list_str = OrderedStringList(False)
        self.o_list_str.add("ab")
        self.o_list_str.add("ad")
        self.o_list_str.add("ae")        
        self.o_list_str.add("  aa")
        res = get_list_nodes(self.o_list_str)
        self.assertEqual(res, ["ae", "ad", "ab", "  aa"])        
    
    def test_find(self):
        self.o_list_str = OrderedStringList(True)
        self.o_list_str.add("ab")
        self.o_list_str.add("ad")
        self.o_list_str.add("ae")
        self.o_list_str.add(" ac  ")        
        self.assertEqual(self.o_list_str.find("ad").value, "ad") 
        
        self.o_list_str = OrderedStringList(False)
        self.o_list_str.add("ab")
        self.o_list_str.add("ad")
        self.o_list_str.add("ae")
        self.o_list_str.add(" ac  ")        
        self.assertEqual(self.o_list_str.find("ad").value, "ad") 
        
        self.o_list_str = OrderedStringList(False)
        self.assertEqual(self.o_list_str.find("ad"), None)   
        
    def test_delete(self):
        self.o_list_str = OrderedStringList(True)
        self.o_list_str.add("ab")
        self.o_list_str.add("ad")
        self.o_list_str.add("ae")
        self.o_list_str.add(" ac  ")  
        self.o_list_str.delete(" ac  ")
        res = get_list_nodes(self.o_list_str)
        self.assertEqual(res, ["ab", "ad", "ae"])        
      
if __name__ == '__main__':
    unittest.main()        
   
