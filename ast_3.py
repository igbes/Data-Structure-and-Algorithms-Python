import unittest
from ast_2 import get_tree_ast

def is_digit(string):
    """Вспомогательная функция, проверяет, 
    содержит ли строка только число
    """
    try:
        float(string)
        return True
    except ValueError:
        return False
    
def is_result(item):
    """Вспомогательная функция, проверяет,
    является ли аргумент списком или строкой, содержащей
    только число
    """
    if isinstance(item, list):
        return True
    if is_digit(item):
        return True
    else:
        return False
    
def get_result(st):
    """Возвращает список из двух элементов: 
    первым идет результат интерпретации, 
    вторым - результат трансляции
    """
    tree = get_tree_ast(st)
    
    def iter(tr):
        if tr.level == 0 and isinstance(tr.value, list):
            if tr.value[0].isdigit():
                res = int(tr.value[0])
            else:
                res = float(tr.value[0])
            return [res, tr.value[1]]
        
        if tr.level == 0 and is_digit(tr.value):
            if tr.value.isdigit():
                res = int(tr.value)
            else:
                res = float(tr.value)
            return [res, str(res)] 
        
        if is_result(tr.child[0].value) and is_result(tr.child[1].value):
            res = []
            res_2 = []
            i = 0
            for elem in tr.child:
                if i == 1:
                    res.append(tr.value)
                    res_2.append(tr.value)
                if isinstance(elem.value, list):
                    res.append(elem.value[0])
                    res_2.append(elem.value[1])
                    i += 1
                elif is_digit(elem.value):
                    res.append(elem.value)
                    res_2.append(elem.value)
                    i += 1
                    
            res_2 = '(' + ''.join(res_2) + ')'
            tr.value = [str(eval(''.join(res))), res_2]
            tr.child.pop()
            tr.child.pop()            
            if tr.level > 0:
                tr = tr.parent
            return iter(tr) 
              
        if len(tr.child) == 2:
            for element in tr.child:
                if not is_result(element.value):
                    return iter(element)
                
    return iter(tree.root)

class TestGetResult(unittest.TestCase):
    
    def test_get_result(self):
        
        st = "8"
        self.assertEqual(get_result(st), [8, '8'])         
        
        st = '3+(5-7)'
        self.assertEqual(get_result(st), [1, '(3+(5-7))'])        
        
        st = '((7+3)*(5-2))'
        self.assertEqual(get_result(st), [30, '((7+3)*(5-2))']) 
        
        st = "71+32/25*(5-2*89+14)/65-21"
        self.assertEqual(get_result(st), [46.868923076923075, '(71+(((32/25)*(((5-(2*89))+14)/65))-21))'])
        
if __name__ == '__main__':
    unittest.main()     
